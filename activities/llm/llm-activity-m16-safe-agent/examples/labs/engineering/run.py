"""CLI for application labs. Ollama commands require a running local service."""
import argparse
import json
from pathlib import Path
import sys
from .client import Ollama, ChatSession, Cancelled
from .rag import RAG, evaluate
from .agent import run_agent
from .mcp import Client

FIXTURES = Path(__file__).parent / "fixtures"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["chat", "rag", "rag-eval", "agent", "mcp-check"])
    parser.add_argument("--model")
    parser.add_argument("--embedding-model")
    parser.add_argument("--prompt", default="Quanti posti ha LAB-A?")
    parser.add_argument("--mcp", action="store_true")
    parser.add_argument("--interactive", action="store_true", help="multi-turn chat; /quit or Ctrl-C to exit")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.command != "mcp-check" and not args.model:
        parser.error("--model is required for Ollama operations")
    if args.command.startswith("rag") and not args.embedding_model:
        parser.error("--embedding-model is required for dense retrieval")
    try:
        inventory, embedding_inventory = None, None
        if args.command == "mcp-check":
            with Client() as client:
                result = {"transport": "real-local-stdio", "tools": client.request("tools/list", {}),
                          "result": client.lookup({"room": "LAB-A"})}
        else:
            provider = Ollama(args.model)
            inventory = provider.inventory()
            if args.command == "chat":
                session = ChatSession(provider)
                turns = []
                prompt = args.prompt
                while True:
                    turns.append(session.send(prompt, on_chunk=lambda x: print(x, end="", file=sys.stderr, flush=True)))
                    print(file=sys.stderr)
                    if not args.interactive:
                        break
                    try:
                        prompt = input("Tu (/quit): ")
                    except (EOFError, KeyboardInterrupt):
                        break
                    if prompt.strip() == "/quit":
                        break
                result = {"turns": turns}
            elif args.command.startswith("rag"):
                embedder = Ollama(args.embedding_model)
                embedding_inventory = embedder.inventory()
                rag = RAG(json.loads((FIXTURES / "documents.json").read_text()),
                          embedder, provider)
                result = rag.answer(args.prompt) if args.command == "rag" else evaluate(
                    rag, json.loads((FIXTURES / "rag-eval.json").read_text()))
            elif args.mcp:
                with Client() as client:
                    result = run_agent(provider, args.prompt, execute=client.lookup)
            else:
                result = run_agent(provider, args.prompt)
        report = {"model": args.model, "embedding_model": args.embedding_model,
                  "inventory": inventory, "embedding_inventory": embedding_inventory,
                  "prompt": args.prompt,
                  "mode": "real-local-stdio" if args.command == "mcp-check" else "live-local", "result": result}
        text = json.dumps(report, ensure_ascii=False, indent=2)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(text + "\n")
        print(text)
    except (OSError, ValueError, KeyError, Cancelled, KeyboardInterrupt) as error:
        parser.exit(1, f"Operation failed or cancelled: {type(error).__name__}: {error}\n")


if __name__ == "__main__":
    main()
