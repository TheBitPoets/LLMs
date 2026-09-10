#!/usr/bin/env python3
"""Ask a local Ollama model for a booking DRAFT; never create a booking.

This is a single LLM request, not a coding-agent harness. A fake response is
used by unit tests. Actual latency and model quality require a local run.
"""
import argparse
import json
import urllib.request

SCHEMA = {
    "type": "object", "additionalProperties": False,
    "required": ["room", "start", "end"],
    "properties": {
        "room": {"type": "string", "enum": ["LAB-A", "LAB-B"]},
        "start": {"type": "integer", "minimum": 480, "maximum": 1079},
        "end": {"type": "integer", "minimum": 481, "maximum": 1080},
    },
}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def parse_proposal(content):
    value = json.loads(content, object_pairs_hook=unique_object)
    if not isinstance(value, dict) or set(value) != {"room", "start", "end"}:
        raise ValueError("expected exactly room, start and end")
    if value["room"] not in ("LAB-A", "LAB-B"):
        raise ValueError("unknown room")
    start, end = value["start"], value["end"]
    if type(start) is not int or type(end) is not int:
        raise ValueError("integer minutes required")
    if not 480 <= start < end <= 1080 or end - start > 180:
        raise ValueError("invalid interval")
    return value


def propose(model, text, timeout=60):
    body = {
        "model": model, "stream": False, "format": SCHEMA,
        "options": {"temperature": 0, "seed": 7, "num_predict": 120},
        "messages": [
            {"role": "system", "content": (
                "Convert a single-day classroom booking request to JSON. "
                "Minutes since midnight; rooms LAB-A or LAB-B. "
                "Return only room, start, end. This is a proposal, not a reservation."
            )},
            {"role": "user", "content": text},
        ],
    }
    request = urllib.request.Request(
        "http://127.0.0.1:11434/api/chat", data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"}, method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        answer = json.load(response)
    draft = parse_proposal(answer["message"]["content"])
    return {"status": "draft_requires_review", "draft": draft,
            "model": answer.get("model", model),
            "eval_count": answer.get("eval_count"),
            "eval_duration_ns": answer.get("eval_duration"),
            "total_duration_ns": answer.get("total_duration")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True)
    parser.add_argument("--text", required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(propose(args.model, args.text), indent=2, ensure_ascii=False))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"Proposal unavailable or invalid: {error}\n")


if __name__ == "__main__":
    main()
