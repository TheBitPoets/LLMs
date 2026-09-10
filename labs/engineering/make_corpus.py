"""Generate original synthetic sentences with disjoint document-level splits."""
from pathlib import Path


def corpora():
    rows = [(f"{name} studia {topic} nel laboratorio {room}.\n")
            for name in ["Ada", "Luca", "Mia", "Nico", "Sara", "Toni"]
            for topic in ["python", "reti", "dati", "robotica"]
            for room in ["A", "B", "C"]]
    adapted = [(f"scheda: aula={room}; posti={seats}; attivita={topic}.\n")
               for room in ["A", "B", "C", "D"]
               for seats in [12, 18, 24, 30]
               for topic in ["python", "reti", "robotica"]]
    result = {}
    for prefix, source in [("base", rows), ("adapt", adapted)]:
        for split, residues in [("train", {0, 1, 2, 3, 4, 5, 6}), ("valid", {7, 8}), ("test", {9})]:
            result[f"{prefix}-{split}.txt"] = "".join(row for i, row in enumerate(source) if i % 10 in residues)
    return result


if __name__ == "__main__":
    root = Path(__file__).parent / "fixtures/text"
    root.mkdir(parents=True, exist_ok=True)
    for name, text in corpora().items():
        (root / name).write_text(text, encoding="utf-8")
    print("Six original synthetic corpus splits written")
