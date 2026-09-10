#!/usr/bin/env python3
"""Laboratori LLM riproducibili con sola libreria standard."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import os
import platform
import random
import re
import statistics
import time
import urllib.error
import urllib.request
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent


def stable_softmax(logits: list[float], temperature: float = 1.0) -> list[float]:
    if not logits:
        raise ValueError("logits non può essere vuoto")
    if not math.isfinite(temperature) or temperature <= 0:
        raise ValueError("temperature deve essere finita e > 0")
    scaled = [x / temperature for x in logits]
    if not all(math.isfinite(x) for x in scaled):
        raise ValueError("i logits devono essere finiti")
    maximum = max(scaled)
    exponentials = [math.exp(x - maximum) for x in scaled]
    total = sum(exponentials)
    return [x / total for x in exponentials]


def bytes_report(text: str) -> dict[str, Any]:
    raw = text.encode("utf-8")
    return {
        "text": text,
        "characters": len(text),
        "code_points": [f"U+{ord(c):04X}" for c in text],
        "utf8_bytes": list(raw),
        "utf8_hex": raw.hex(" "),
        "byte_count": len(raw),
        "round_trip": raw.decode("utf-8") == text,
    }


def gradient_demo(steps: int, learning_rate: float) -> dict[str, Any]:
    if steps < 1 or steps > 10_000:
        raise ValueError("steps deve essere tra 1 e 10000")
    if not math.isfinite(learning_rate) or learning_rate <= 0:
        raise ValueError("learning-rate deve essere finito e > 0")
    # Dataset y = 2x; il bias è omesso per rendere visibile il gradiente.
    xs, ys, weight = [1.0, 2.0, 3.0], [2.0, 4.0, 6.0], 0.0
    history = []
    for step in range(steps):
        predictions = [weight * x for x in xs]
        errors = [p - y for p, y in zip(predictions, ys)]
        loss = sum(e * e for e in errors) / len(xs)
        gradient = 2 * sum(e * x for e, x in zip(errors, xs)) / len(xs)
        history.append({"step": step, "weight": weight, "loss": loss, "gradient": gradient})
        weight -= learning_rate * gradient
    final_loss = sum((weight * x - y) ** 2 for x, y in zip(xs, ys)) / len(xs)
    return {"learning_rate": learning_rate, "history": history, "final_weight": weight, "final_loss": final_loss}


def attention_demo(causal: bool = True) -> dict[str, Any]:
    q = [1.0, 0.5]
    keys = [[1.0, 0.0], [0.5, 1.0], [1.0, 1.0]]
    values = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
    query_position = 1
    scores = [sum(a * b for a, b in zip(q, k)) / math.sqrt(2) for k in keys]
    masked = [(-math.inf if causal and i > query_position else s) for i, s in enumerate(scores)]
    finite = [s for s in masked if math.isfinite(s)]
    maximum = max(finite)
    exps = [math.exp(s - maximum) if math.isfinite(s) else 0.0 for s in masked]
    weights = [x / sum(exps) for x in exps]
    output = [sum(weights[i] * values[i][d] for i in range(len(values))) for d in range(2)]
    return {"query": q, "keys": keys, "values": values, "scores": scores, "causal": causal, "weights": weights, "output": output}


def memory_estimate(parameters_b: float, bits: int, context_k: int, available_gb: float) -> dict[str, Any]:
    if parameters_b <= 0 or bits not in {2, 3, 4, 5, 6, 8, 16, 32} or context_k <= 0 or available_gb <= 0:
        raise ValueError("parametri di memoria non validi")
    weights = parameters_b * bits / 8
    runtime = max(1.2, weights * 0.12)
    kv_placeholder = context_k * 0.045
    total = weights + runtime + kv_placeholder
    return {
        "parameters_b": parameters_b,
        "bits": bits,
        "context_k": context_k,
        "weights_gb_decimal": weights,
        "runtime_margin_gb": runtime,
        "kv_placeholder_gb": kv_placeholder,
        "estimated_total_gb": total,
        "available_gb": available_gb,
        "fits_with_15_percent_headroom": total <= available_gb * 0.85,
        "warning": "Stima didattica: misurare architettura, KV cache e runtime reali.",
    }


def truncate_distribution(probabilities: list[float], top_k: int | None, top_p: float | None) -> list[float]:
    if not probabilities or any(p < 0 or not math.isfinite(p) for p in probabilities):
        raise ValueError("probabilità non valide")
    total = sum(probabilities)
    if total <= 0:
        raise ValueError("la massa deve essere positiva")
    normalized = [p / total for p in probabilities]
    order = sorted(range(len(normalized)), key=lambda i: normalized[i], reverse=True)
    keep = order[: max(1, min(top_k, len(order)))] if top_k else order[:]
    if top_p is not None:
        if not 0 < top_p <= 1:
            raise ValueError("top-p deve essere in (0,1]")
        cumulative, nucleus = 0.0, []
        for i in keep:
            nucleus.append(i)
            cumulative += normalized[i]
            if cumulative >= top_p:
                break
        keep = nucleus
    result = [normalized[i] if i in keep else 0.0 for i in range(len(normalized))]
    kept_total = sum(result)
    return [p / kept_total for p in result]


def sampling_demo(seed: int, draws: int, temperature: float, top_k: int | None, top_p: float | None) -> dict[str, Any]:
    if draws < 1 or draws > 1_000_000:
        raise ValueError("draws fuori limite")
    labels, logits = ["blu", "sereno", "grigio", "immenso"], [2.1, 1.25, 0.9, 0.25]
    probabilities = truncate_distribution(stable_softmax(logits, temperature), top_k, top_p)
    rng = random.Random(seed)
    samples = rng.choices(labels, weights=probabilities, k=draws)
    counts = Counter(samples)
    return {"seed": seed, "draws": draws, "temperature": temperature, "top_k": top_k, "top_p": top_p, "probabilities": dict(zip(labels, probabilities)), "counts": dict(counts)}


def evaluate_jsonl(path: Path) -> dict[str, Any]:
    rows = []
    with path.open(encoding="utf-8") as stream:
        for line_no, line in enumerate(stream, 1):
            if line.strip():
                row = json.loads(line)
                for field in ("id", "category", "expected", "predicted"):
                    if field not in row:
                        raise ValueError(f"riga {line_no}: manca {field}")
                rows.append(row)
    if not rows:
        raise ValueError("dataset vuoto")
    by_category: dict[str, list[bool]] = {}
    errors = []
    for row in rows:
        correct = str(row["expected"]).strip().casefold() == str(row["predicted"]).strip().casefold()
        by_category.setdefault(str(row["category"]), []).append(correct)
        if not correct:
            errors.append({"id": row["id"], "category": row["category"], "expected": row["expected"], "predicted": row["predicted"]})
    return {"examples": len(rows), "accuracy": 1 - len(errors) / len(rows), "by_category": {k: sum(v) / len(v) for k, v in by_category.items()}, "errors": errors}


def terms(text: str) -> list[str]:
    return re.findall(r"[a-zà-öø-ÿ0-9]+", text.casefold())


def tiny_rag(query: str, corpus_path: Path, k: int = 3) -> dict[str, Any]:
    query_terms = Counter(terms(query))
    documents = json.loads(corpus_path.read_text(encoding="utf-8"))
    scored = []
    for document in documents:
        doc_terms = Counter(terms(document["text"]))
        overlap = sum(min(count, doc_terms[token]) for token, count in query_terms.items())
        score = overlap / math.sqrt(max(1, sum(query_terms.values()) * sum(doc_terms.values())))
        scored.append({**document, "score": score})
    ranked = sorted(scored, key=lambda x: (-x["score"], x["id"]))[:k]
    answerable = bool(ranked and ranked[0]["score"] > 0)
    return {"query": query, "answerable": answerable, "citations": [x["id"] for x in ranked if x["score"] > 0], "results": ranked}


ALLOWED_BINOPS = {ast.Add: lambda a, b: a + b, ast.Sub: lambda a, b: a - b, ast.Mult: lambda a, b: a * b, ast.Div: lambda a, b: a / b}
ALLOWED_UNARY = {ast.UAdd: lambda a: a, ast.USub: lambda a: -a}


def safe_calculate(expression: str) -> float:
    tree = ast.parse(expression, mode="eval")
    def visit(node: ast.AST) -> float:
        if isinstance(node, ast.Expression): return visit(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)): return float(node.value)
        if isinstance(node, ast.BinOp) and type(node.op) in ALLOWED_BINOPS: return ALLOWED_BINOPS[type(node.op)](visit(node.left), visit(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in ALLOWED_UNARY: return ALLOWED_UNARY[type(node.op)](visit(node.operand))
        raise ValueError(f"operazione non consentita: {type(node).__name__}")
    result = visit(tree)
    if not math.isfinite(result) or abs(result) > 1e100:
        raise ValueError("risultato fuori limite")
    return result


def safe_agent(request: str) -> dict[str, Any]:
    match = re.fullmatch(r"\s*CALCOLA\s*:\s*(.{1,120})\s*", request, re.IGNORECASE)
    if not match:
        return {"decision": "reject", "reason": "schema richiesto: CALCOLA: <espressione>", "tool_calls": 0}
    try:
        result = safe_calculate(match.group(1))
    except (SyntaxError, ValueError, ZeroDivisionError) as exc:
        return {"decision": "reject", "reason": str(exc), "tool_calls": 0}
    return {"decision": "execute", "tool": "calculator.read_only", "arguments": {"expression": match.group(1)}, "result": result, "tool_calls": 1}


def probability_a(prefix: str) -> Fraction:
    state = 17
    for char in prefix:
        state = (state * 31 + ord(char)) & 0xFFFFFFFF
    return Fraction(20 + state % 61, 100)


def arithmetic_encode(message: str) -> dict[str, Any]:
    message = message.upper()
    if not message or len(message) > 64 or set(message) - {"A", "B"}:
        raise ValueError("message deve contenere 1-64 simboli A/B")
    low, high, trace = Fraction(0), Fraction(1), []
    for position, symbol in enumerate(message):
        probability = probability_a(message[:position])
        split = low + (high - low) * probability
        trace.append({"position": position, "prefix": message[:position], "symbol": symbol, "p_a": float(probability), "low": float(low), "split": float(split), "high": float(high)})
        if symbol == "A": high = split
        else: low = split
    for length in range(1, 257):
        scale = 1 << length
        numerator = (low.numerator * scale + low.denominator - 1) // low.denominator
        value = Fraction(numerator, scale)
        if value < high:
            bits = format(numerator, f"0{length}b")
            break
    else:
        raise ValueError("intervallo troppo stretto")
    decoded = arithmetic_decode(bits, len(message))
    return {"message": message, "bits": bits, "bit_count": len(bits), "final_interval": [float(low), float(high)], "decoded": decoded, "round_trip": decoded == message, "sha256": hashlib.sha256(message.encode()).hexdigest(), "decoded_sha256": hashlib.sha256(decoded.encode()).hexdigest(), "trace": trace}


def arithmetic_decode(bits: str, length: int) -> str:
    if not bits or set(bits) - {"0", "1"}:
        raise ValueError("bitstream non valido")
    value = Fraction(int(bits, 2), 1 << len(bits))
    low, high, result = Fraction(0), Fraction(1), ""
    for _ in range(length):
        split = low + (high - low) * probability_a(result)
        if value < split:
            result += "A"; high = split
        else:
            result += "B"; low = split
    return result


def system_manifest() -> dict[str, Any]:
    memory = None
    try:
        pages = os.sysconf("SC_PHYS_PAGES"); page_size = os.sysconf("SC_PAGE_SIZE")
        memory = pages * page_size
    except (AttributeError, ValueError, OSError):
        pass
    return {"platform": platform.platform(), "python": platform.python_version(), "machine": platform.machine(), "processor": platform.processor() or "unknown", "memory_bytes": memory, "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


def ollama_generate(model: str, prompt: str, host: str, timeout: float) -> dict[str, Any]:
    if not host.startswith(("http://127.0.0.1", "http://localhost")):
        raise ValueError("il laboratorio base accetta solo un host Ollama locale")
    payload = json.dumps({"model": model, "prompt": prompt, "stream": False, "options": {"temperature": 0, "seed": 7}}).encode()
    request = urllib.request.Request(host.rstrip("/") + "/api/generate", data=payload, headers={"Content-Type": "application/json"})
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            result = json.load(response)
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError(f"Ollama non raggiungibile: {exc}") from exc
    result["wall_seconds_client"] = time.perf_counter() - started
    result["requested_model"] = model
    result["host"] = host
    return result


def ollama_benchmark(model: str, host: str, timeout: float) -> dict[str, Any]:
    prompts = ["Rispondi solo: OK", "Elenca tre numeri primi minori di dieci.", "In una frase, distingui RAM e spazio su disco."]
    runs = [ollama_generate(model, prompt, host, timeout) for prompt in prompts]
    walls = [run["wall_seconds_client"] for run in runs]
    return {"model": model, "host": host, "runs": runs, "median_wall_seconds": statistics.median(walls), "warning": "Tre fixture sono uno smoke test, non una valutazione di qualità."}


def emit(report: dict[str, Any], output: str | None) -> None:
    serialized = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True)
    if output:
        destination = Path(output)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(serialized + "\n", encoding="utf-8")
    print(serialized)


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    root.add_argument("--output", dest="global_output", help="salva anche il report JSON")
    commands = root.add_subparsers(dest="command", required=True)
    commands.add_parser("system")
    soft = commands.add_parser("softmax"); soft.add_argument("--logits", nargs="+", type=float, required=True); soft.add_argument("--temperature", type=float, default=1)
    byte = commands.add_parser("bytes"); byte.add_argument("--text", required=True)
    grad = commands.add_parser("gradient"); grad.add_argument("--steps", type=int, default=12); grad.add_argument("--learning-rate", type=float, default=0.1)
    attn = commands.add_parser("attention"); attn.add_argument("--no-causal", action="store_true")
    mem = commands.add_parser("memory"); mem.add_argument("--parameters", type=float, required=True); mem.add_argument("--bits", type=int, default=4); mem.add_argument("--context-k", type=int, default=8); mem.add_argument("--available", type=float, required=True)
    sample = commands.add_parser("sample"); sample.add_argument("--seed", type=int, default=7); sample.add_argument("--draws", type=int, default=100); sample.add_argument("--temperature", type=float, default=1); sample.add_argument("--top-k", type=int); sample.add_argument("--top-p", type=float)
    evaluate = commands.add_parser("evaluate"); evaluate.add_argument("--predictions", type=Path, required=True)
    rag = commands.add_parser("rag"); rag.add_argument("--query", required=True); rag.add_argument("--corpus", type=Path, default=ROOT / "fixtures" / "rag-corpus.json"); rag.add_argument("-k", type=int, default=3)
    agent = commands.add_parser("agent"); agent.add_argument("--request", required=True)
    pol = commands.add_parser("pollicino"); pol.add_argument("--message", required=True)
    for name in ("ollama", "benchmark"):
        cmd = commands.add_parser(name); cmd.add_argument("--model", required=True); cmd.add_argument("--host", default="http://127.0.0.1:11434"); cmd.add_argument("--timeout", type=float, default=120)
        if name == "ollama": cmd.add_argument("--prompt", required=True)
    for command in commands.choices.values():
        command.add_argument("--output", dest="command_output", help="salva anche il report JSON")
    return root


def main() -> None:
    args = parser().parse_args()
    if args.command == "system": report = system_manifest()
    elif args.command == "softmax": report = {"probabilities": stable_softmax(args.logits, args.temperature), "sum": sum(stable_softmax(args.logits, args.temperature))}
    elif args.command == "bytes": report = bytes_report(args.text)
    elif args.command == "gradient": report = gradient_demo(args.steps, args.learning_rate)
    elif args.command == "attention": report = attention_demo(not args.no_causal)
    elif args.command == "memory": report = memory_estimate(args.parameters, args.bits, args.context_k, args.available)
    elif args.command == "sample": report = sampling_demo(args.seed, args.draws, args.temperature, args.top_k, args.top_p)
    elif args.command == "evaluate": report = evaluate_jsonl(args.predictions)
    elif args.command == "rag": report = tiny_rag(args.query, args.corpus, args.k)
    elif args.command == "agent": report = safe_agent(args.request)
    elif args.command == "pollicino": report = arithmetic_encode(args.message)
    elif args.command == "ollama": report = ollama_generate(args.model, args.prompt, args.host, args.timeout)
    else: report = ollama_benchmark(args.model, args.host, args.timeout)
    emit(report, getattr(args, "command_output", None) or args.global_output)


if __name__ == "__main__":
    main()
