"""Deterministic exam diagnostics; factual assessment stays with the teacher."""
import argparse
import importlib.util
import json
from pathlib import Path


def score(predictions, cases, key, validate):
    if not isinstance(predictions, list):
        raise ValueError("submission must be a JSON list")
    ids = [p.get("id") if isinstance(p, dict) else None for p in predictions]
    expected_ids = {c["id"] for c in cases}
    if (any(not isinstance(i, str) for i in ids) or len(set(ids)) != len(ids)
            or set(ids) - expected_ids):
        raise ValueError("duplicate, unknown or invalid case IDs")
    if set(key) != expected_ids:
        raise ValueError("key does not match cases")
    by_id = dict(zip(ids, predictions))
    rows = []
    for case in cases:
        cid = case["id"]
        row = {"id": cid, "schema_valid": False, "source_set_correct": False,
               "abstention_correct": False, "factual_review": "pending"}
        try:
            result = by_id[cid]
            validate(result, case["source_ids"])
            row["schema_valid"] = True
            sources = {point["source_id"] for point in result["points"]}
            row["source_set_correct"] = sources == set(key[cid]["sources"])
            row["abstention_correct"] = result["abstained"] == (not key[cid]["sources"])
        except (KeyError, ValueError) as error:
            row["error"] = "missing case" if cid not in by_id else str(error)
        rows.append(row)
    denominator = len(cases)
    return {"cases": rows, "case_count": denominator,
            "valid_schema_fraction": sum(r["schema_valid"] for r in rows)/denominator,
            "correct_source_set_fraction": sum(r["source_set_correct"] for r in rows)/denominator,
            "correct_abstention_fraction": sum(r["abstention_correct"] for r in rows)/denominator,
            "factual_accuracy": None, "final_grade": None,
            "limits": "source IDs do not prove factual support; teacher rubric required"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("submission", type=Path)
    parser.add_argument("--student-dir", type=Path, required=True)
    parser.add_argument("--key", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("output exists; choose a new report path")
    spec = importlib.util.spec_from_file_location("exam_contract", args.student_dir/"contract.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    report = score(json.loads(args.submission.read_text()),
                   json.loads((args.student_dir/"cases.json").read_text()),
                   json.loads(args.key.read_text()), module.validate)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({k:v for k,v in report.items() if k != "cases"}))


if __name__ == "__main__":
    main()
