"""Bounded local Ollama transport and transactional conversation history."""
from __future__ import annotations

import json
import math
import threading
import time
import platform
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


class ProtocolError(ValueError):
    pass


class Cancelled(Exception):
    pass


class Ollama:
    def __init__(self, model, host="http://127.0.0.1:11434", timeout=30, max_bytes=2_000_000):
        url = urlsplit(host)
        if (url.scheme != "http" or url.hostname not in {"localhost", "127.0.0.1", "::1"}
                or url.username or url.password or url.path not in {"", "/"}
                or url.query or url.fragment):
            raise ValueError("a loopback HTTP origin is required")
        if not isinstance(model, str) or not model.strip() or timeout <= 0 or max_bytes < 1:
            raise ValueError("invalid model or transport limits")
        self.model, self.host, self.timeout, self.max_bytes = model, host.rstrip("/"), timeout, max_bytes

    def _request(self, endpoint, payload):
        return Request(self.host + endpoint, data=json.dumps(payload).encode(),
                       headers={"Content-Type": "application/json"}, method="POST")

    def post(self, endpoint, payload):
        with urlopen(self._request(endpoint, payload), timeout=self.timeout) as response:
            data = response.read(self.max_bytes + 1)
        if len(data) > self.max_bytes:
            raise ProtocolError("response exceeds byte budget")
        value = json.loads(data)
        if not isinstance(value, dict) or "error" in value:
            raise ProtocolError("Ollama error or invalid envelope")
        return value

    def payload(self, messages, stream=False, tools=None):
        result = {"model": self.model, "messages": messages, "stream": stream,
                  "options": {"temperature": 0, "seed": 7, "num_predict": 256}}
        if tools is not None:
            result["tools"] = tools
        return result

    def inventory(self):
        values = {}
        for endpoint in ["version", "tags"]:
            with urlopen(self.host + "/api/" + endpoint, timeout=self.timeout) as response:
                data = response.read(self.max_bytes+1)
            if len(data) > self.max_bytes:
                raise ProtocolError("inventory exceeds byte budget")
            values[endpoint] = json.loads(data)
            if not isinstance(values[endpoint], dict) or "error" in values[endpoint]:
                raise ProtocolError("invalid inventory response")
        if (not isinstance(values["version"].get("version"), str)
                or not isinstance(values["tags"].get("models"), list)
                or any(not isinstance(m, dict) for m in values["tags"]["models"])):
            raise ProtocolError("invalid version or model list")
        models = [m for m in values["tags"].get("models", [])
                  if m.get("name") in {self.model, self.model+":latest"}]
        if not models or any(not m.get("digest") for m in models):
            raise ProtocolError("model not found in local inventory with a digest")
        return {"ollama_version": values["version"].get("version"), "model": self.model,
                "local_artifacts": models, "python": platform.python_version(),
                "machine": platform.machine(), "system": platform.system(),
                "parameters": self.payload([])["options"], "host": self.host}

    def complete(self, messages, tools=None, format=None):
        payload = self.payload(messages, tools=tools)
        if format is not None:
            payload["format"] = format
        result = self.post("/api/chat", payload)
        if result.get("done") is not True or not isinstance(result.get("message"), dict):
            raise ProtocolError("incomplete chat response")
        return result

    def stream(self, messages, cancel):
        if cancel.is_set():
            raise Cancelled()
        total = 0
        with urlopen(self._request("/api/chat", self.payload(messages, stream=True)),
                     timeout=self.timeout) as response:
            while True:
                if cancel.is_set():
                    raise Cancelled()
                line = response.readline(self.max_bytes - total + 1)
                if not line:
                    raise ProtocolError("stream ended without done=true")
                total += len(line)
                if total > self.max_bytes:
                    raise ProtocolError("stream exceeds byte budget")
                value = json.loads(line)
                if not isinstance(value, dict) or "error" in value:
                    raise ProtocolError("invalid stream envelope")
                message = value.get("message", {})
                if not isinstance(message, dict) or not isinstance(message.get("content", ""), str):
                    raise ProtocolError("invalid content chunk")
                yield value
                if value.get("done") is True:
                    return

    def embed(self, texts):
        value = self.post("/api/embed", {"model": self.model, "input": texts, "truncate": False})
        vectors = value.get("embeddings")
        if not isinstance(vectors, list) or len(vectors) != len(texts):
            raise ProtocolError("wrong embedding count")
        width = len(vectors[0]) if vectors and isinstance(vectors[0], list) else 0
        if not width or any(not isinstance(v, list) or len(v) != width or
                            any(type(x) not in (int, float) or not math.isfinite(x) for x in v)
                            for v in vectors):
            raise ProtocolError("invalid embedding vectors")
        return vectors


class ChatSession:
    def __init__(self, provider, system="Rispondi in italiano.", max_chars=12000):
        self.provider, self.max_chars = provider, max_chars
        self.system = {"role": "system", "content": system}
        self.history = []
        self.state = "idle"

    def send(self, text, on_chunk=lambda _: None, cancel=None):
        if self.state == "streaming":
            raise RuntimeError("one active request per session")
        if not isinstance(text, str) or not text.strip():
            raise ValueError("nonempty user message required")
        cancel = cancel or threading.Event()
        history = list(self.history)
        messages = [self.system, *history, {"role": "user", "content": text}]
        while sum(len(m["content"]) for m in messages) > self.max_chars and history:
            history = history[2:]
            messages = [self.system, *history, {"role": "user", "content": text}]
        if sum(len(m["content"]) for m in messages) > self.max_chars:
            raise ValueError("current turn exceeds character budget")
        self.state = "streaming"
        start, ttft, chunks, final = time.perf_counter(), None, [], None
        stream = self.provider.stream(messages, cancel)
        try:
            for item in stream:
                if cancel.is_set():
                    raise Cancelled()
                content = item.get("message", {}).get("content", "")
                if content:
                    if ttft is None:
                        ttft = time.perf_counter() - start
                    chunks.append(content)
                    on_chunk(content)
                if item.get("done"):
                    final = item
            if cancel.is_set():
                raise Cancelled()
            if final is None:
                raise ProtocolError("missing final message")
            answer = "".join(chunks)
            self.history = [*history, {"role": "user", "content": text},
                            {"role": "assistant", "content": answer}]
            self.state = "idle"
            return {"answer": answer, "ttft_seconds": ttft,
                    "elapsed_seconds": time.perf_counter() - start,
                    "eval_count": final.get("eval_count"),
                    "eval_duration_ns": final.get("eval_duration")}
        except (Cancelled, KeyboardInterrupt):
            self.state = "cancelled"
            raise
        except Exception:
            self.state = "error"
            raise
        finally:
            stream.close()
