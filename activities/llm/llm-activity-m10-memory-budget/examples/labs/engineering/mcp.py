"""Minimal MCP 2025-06-18 stdio tools server/client, implemented for teaching.

Only initialize, initialized, ping, tools/list and tools/call are supported.
No network transport, resource subscriptions or arbitrary process tool.
"""
import json
import queue
import subprocess
import sys
import threading
from .agent import TOOL, lookup_room

VERSION = "2025-06-18"


class Server:
    def __init__(self):
        self.initialized = False
        self.negotiated = False

    def handle(self, message):
        if not isinstance(message, dict) or message.get("jsonrpc") != "2.0":
            return {"jsonrpc": "2.0", "id": None, "error": {"code": -32600, "message": "Invalid Request"}}
        request_id, method, params = message.get("id"), message.get("method"), message.get("params", {})
        notification = "id" not in message
        if notification:
            if method == "notifications/initialized" and self.negotiated:
                self.initialized = True
            return None
        result, error = None, None
        try:
            if not isinstance(params, dict):
                raise ValueError("params must be an object")
            if method == "initialize":
                if self.negotiated:
                    raise ValueError("already initialized")
                if not isinstance(params.get("protocolVersion"), str):
                    raise ValueError("protocolVersion required")
                self.negotiated = True
                result = {"protocolVersion": VERSION, "capabilities": {"tools": {"listChanged": False}},
                          "serverInfo": {"name": "course-room-catalogue", "version": "1.0.0"}}
            elif method == "ping":
                result = {}
            elif not self.initialized:
                error = {"code": -32002, "message": "Initialization required"}
            elif method == "tools/list":
                f = TOOL["function"]
                result = {"tools": [{"name": f["name"], "description": f["description"],
                          "inputSchema": f["parameters"], "annotations": {"readOnlyHint": True}}]}
            elif method == "tools/call":
                if params.get("name") != "lookup_room":
                    raise ValueError("unknown tool")
                try:
                    data = lookup_room(params.get("arguments"))
                    result = {"content": [{"type": "text", "text": json.dumps(data)}],
                              "structuredContent": data, "isError": False}
                except ValueError as exc:
                    result = {"content": [{"type": "text", "text": str(exc)}], "isError": True}
            else:
                error = {"code": -32601, "message": "Method not found"}
        except ValueError as exc:
            error = {"code": -32602, "message": str(exc)}
        return {"jsonrpc": "2.0", "id": request_id, **({"error": error} if error else {"result": result})}


def serve():
    server = Server()
    while True:
        line = sys.stdin.buffer.readline(65537)
        if not line:
            return
        if len(line) > 65536:
            # Close an oversized session; never process a truncated JSON request.
            return
        try:
            response = server.handle(json.loads(line))
        except (ValueError, UnicodeDecodeError):
            response = {"jsonrpc": "2.0", "id": None,
                        "error": {"code": -32700, "message": "Parse error"}}
        if response is not None:
            print(json.dumps(response), flush=True)


class Client:
    def __init__(self, timeout=5):
        self.timeout, self.counter, self.responses = timeout, 0, queue.Queue()
        self.process = subprocess.Popen([sys.executable, "-m", "labs.engineering.mcp"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            text=True, encoding="utf-8")
        self.reader = threading.Thread(target=self._read, daemon=True)
        self.reader.start()
        try:
            result = self.request("initialize", {"protocolVersion": VERSION,
                "capabilities": {}, "clientInfo": {"name": "course-client", "version": "1.0.0"}})
            if result.get("protocolVersion") != VERSION:
                raise ValueError("unsupported negotiated version")
            self._write({"jsonrpc": "2.0", "method": "notifications/initialized"})
        except Exception:
            self.close()
            raise

    def _read(self):
        while True:
            line = self.process.stdout.readline(65537)
            self.responses.put(line)
            if not line or len(line) > 65536:
                return

    def _write(self, message):
        self.process.stdin.write(json.dumps(message) + "\n")
        self.process.stdin.flush()

    def request(self, method, params):
        self.counter += 1
        self._write({"jsonrpc": "2.0", "id": self.counter, "method": method, "params": params})
        try:
            line = self.responses.get(timeout=self.timeout)
        except queue.Empty as exc:
            raise TimeoutError("MCP response timeout") from exc
        if not line or len(line) > 65536:
            raise ValueError("MCP stream closed or response too large")
        value = json.loads(line)
        if value.get("id") != self.counter or value.get("jsonrpc") != "2.0":
            raise ValueError("MCP response ID mismatch")
        if "error" in value:
            raise ValueError(value["error"]["message"])
        return value["result"]

    def lookup(self, arguments):
        result = self.request("tools/call", {"name": "lookup_room", "arguments": arguments})
        if result.get("isError"):
            raise ValueError(result["content"][0]["text"])
        return result["structuredContent"]

    def close(self):
        if self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=self.timeout)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait()
        self.reader.join(timeout=1)
        self.process.stdin.close()
        self.process.stdout.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


if __name__ == "__main__":
    serve()
