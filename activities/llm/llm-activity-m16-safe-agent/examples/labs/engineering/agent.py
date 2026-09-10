"""Actual model tool-call loop with a read-only room-information capability."""
import json

ROOMS = {"LAB-A": {"seats": 24, "equipment": "computer"},
         "LAB-B": {"seats": 18, "equipment": "robotica"}}
TOOL = {"type": "function", "function": {
    "name": "lookup_room", "description": "Read the synthetic classroom catalogue.",
    "parameters": {"type": "object", "properties": {"room": {
        "type": "string", "enum": list(ROOMS)}}, "required": ["room"],
        "additionalProperties": False}}}


def lookup_room(arguments):
    if not isinstance(arguments, dict) or set(arguments) != {"room"}:
        raise ValueError("expected exactly the room argument")
    if arguments["room"] not in ROOMS:
        raise ValueError("unknown room")
    return dict(ROOMS[arguments["room"]])


def run_agent(provider, question, execute=lookup_room, max_steps=4, max_calls=6):
    messages = [{"role": "system", "content": "Usa lookup_room per i dati delle aule. Non inventare dati."},
                {"role": "user", "content": question}]
    trace, cache, calls = [], {}, 0
    for step in range(max_steps):
        response = provider.complete(messages, tools=[TOOL])
        message = response["message"]
        proposals = message.get("tool_calls", [])
        if not isinstance(proposals, list):
            raise ValueError("tool_calls must be a list")
        messages.append(message)
        if not proposals:
            if not isinstance(message.get("content"), str) or not message["content"].strip():
                raise ValueError("empty final answer")
            return {"answer": message["content"], "trace": trace, "steps": step + 1}
        # Validate the complete batch before invoking even read-only tools.
        pending = []
        for call in proposals:
            function = call.get("function", {})
            if function.get("name") != "lookup_room":
                raise ValueError("tool not allowed")
            arguments = function.get("arguments")
            lookup_room(arguments)
            pending.append(arguments)
        if calls + len(pending) > max_calls:
            raise ValueError("tool-call budget exhausted")
        for arguments in pending:
            calls += 1
            key = json.dumps(arguments, sort_keys=True)
            reused = key in cache
            if not reused:
                cache[key] = execute(arguments)
            result = cache[key]
            trace.append({"tool": "lookup_room", "arguments": arguments,
                          "cached": reused, "result": result})
            messages.append({"role": "tool", "tool_name": "lookup_room",
                             "content": json.dumps(result)})
    raise ValueError("agent step budget exhausted")
