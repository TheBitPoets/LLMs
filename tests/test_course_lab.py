import importlib.util
import itertools
import json
import math
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "labs" / "course_lab.py"
SPEC = importlib.util.spec_from_file_location("course_lab", MODULE_PATH)
lab = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(lab)


class CourseLabTests(unittest.TestCase):
    def test_softmax_is_stable_and_normalized(self):
        probabilities = lab.stable_softmax([1000, 999, 998])
        self.assertTrue(all(math.isfinite(x) for x in probabilities))
        self.assertAlmostEqual(sum(probabilities), 1.0)

    def test_softmax_rejects_bad_temperature(self):
        with self.assertRaises(ValueError):
            lab.stable_softmax([1, 2], 0)

    def test_utf8_round_trip_and_emoji_bytes(self):
        report = lab.bytes_report("è🤖")
        self.assertEqual(report["characters"], 2)
        self.assertEqual(report["byte_count"], 6)
        self.assertTrue(report["round_trip"])

    def test_gradient_reduces_loss(self):
        report = lab.gradient_demo(12, 0.1)
        self.assertLess(report["final_loss"], report["history"][0]["loss"])

    def test_causal_attention_masks_future(self):
        report = lab.attention_demo(True)
        self.assertEqual(report["weights"][2], 0)
        self.assertAlmostEqual(sum(report["weights"]), 1.0)

    def test_memory_requires_headroom(self):
        self.assertFalse(lab.memory_estimate(14, 8, 64, 16)["fits_with_15_percent_headroom"])

    def test_sampling_repeats_with_same_seed(self):
        first = lab.sampling_demo(7, 100, 1, 3, 0.9)
        second = lab.sampling_demo(7, 100, 1, 3, 0.9)
        self.assertEqual(first["counts"], second["counts"])

    def test_evaluation_reports_categories(self):
        path = Path(__file__).parents[1] / "labs" / "fixtures" / "predictions.jsonl"
        report = lab.evaluate_jsonl(path)
        self.assertEqual(report["examples"], 6)
        self.assertEqual(len(report["errors"]), 2)

    def test_rag_abstains_without_overlap(self):
        corpus = Path(__file__).parents[1] / "labs" / "fixtures" / "rag-corpus.json"
        report = lab.tiny_rag("xylophone zirconium", corpus)
        self.assertFalse(report["answerable"])

    def test_safe_agent_allows_only_arithmetic(self):
        self.assertEqual(lab.safe_agent("CALCOLA: (12+8)/5")["result"], 4)
        self.assertEqual(lab.safe_agent("CALCOLA: __import__('os').system('id')")["decision"], "reject")

    def test_pollicino_round_trip_exhaustive_to_ten(self):
        for length in range(1, 11):
            for symbols in itertools.product("AB", repeat=length):
                message = "".join(symbols)
                report = lab.arithmetic_encode(message)
                self.assertTrue(report["round_trip"], message)
                self.assertEqual(report["sha256"], report["decoded_sha256"])

    def test_emit_writes_json(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "evidence" / "report.json"
            lab.emit({"ok": True}, str(path))
            self.assertEqual(json.loads(path.read_text()), {"ok": True})


if __name__ == "__main__":
    unittest.main()

