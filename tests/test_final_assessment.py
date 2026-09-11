import copy
import json
from pathlib import Path
import unittest
from labs.final_assessment.student.contract import validate
from labs.final_assessment.teacher.score import score

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "labs/final_assessment"


class FinalAssessmentTests(unittest.TestCase):
    def setUp(self):
        self.notes = json.loads((KIT/"student/notes.json").read_text())
        self.cases = json.loads((KIT/"student/cases.json").read_text())
        self.key = json.loads((KIT/"teacher/key.json").read_text())
        self.answers = [{"id": c["id"], "abstained": not self.key[c["id"]]["sources"],
                         "points": [{"source_id": s, "testo": fact} for s, fact in
                                    zip(self.key[c["id"]]["sources"],self.key[c["id"]]["facts"])]}
                        for c in self.cases]

    def test_twenty_original_notes_and_references(self):
        ids = {n["id"] for n in self.notes}
        self.assertEqual(len(self.notes), 20)
        self.assertEqual(len(ids), 20)
        for c in self.cases:
            self.assertTrue(set(c["source_ids"]) <= ids)
            self.assertTrue(set(self.key[c["id"]]["sources"]) <= set(c["source_ids"]))

    def test_reference_and_semantic_limit(self):
        result = score(self.answers, self.cases, self.key, validate)
        self.assertEqual(result["valid_schema_fraction"], 1)
        self.assertEqual(result["correct_source_set_fraction"], 1)
        wrong = copy.deepcopy(self.answers)
        wrong[0]["points"][1]["testo"] = "La biblioteca chiude alle 23:00."
        report = score(wrong, self.cases, self.key, validate)
        self.assertEqual(report["correct_source_set_fraction"], 1)
        self.assertIsNone(report["factual_accuracy"])
        self.assertIsNone(report["final_grade"])

    def test_missing_cases_count_as_failures(self):
        report = score(self.answers[:1], self.cases, self.key, validate)
        self.assertEqual(report["valid_schema_fraction"], 1/6)
        self.assertEqual(report["case_count"], 6)

    def test_duplicate_unknown_and_malformed_cases(self):
        with self.assertRaises(ValueError):
            score(self.answers+self.answers[:1], self.cases, self.key, validate)
        with self.assertRaises(ValueError):
            score([{"id":"unknown"}], self.cases, self.key, validate)
        for points in [None, [{"source_id":"N99","testo":"X"}]*3,
                       [{"source_id":"N01","testo":"X"}]*3]:
            with self.assertRaises(ValueError):
                validate({"id":"C01","abstained":False,"points":points},["N01","N02","N03"])

    def test_false_astention_and_historical_source(self):
        wrong = copy.deepcopy(self.answers)
        wrong[0]["points"][1]["source_id"] = "N13"
        wrong[1] = {"id":"C02","abstained":True,"points":[]}
        report = score(wrong,self.cases,self.key,validate)
        self.assertTrue(report["cases"][0]["schema_valid"])
        self.assertFalse(report["cases"][0]["source_set_correct"])
        self.assertFalse(report["cases"][1]["abstention_correct"])

    def test_student_export_excludes_exam_key_and_scorer(self):
        path = ROOT/"activities/llm/llm-activity-m19-pollicino/activity.json"
        activity = json.loads(path.read_text())
        public = [a for a in activity["assets"] if a["visibility"] == "student"]
        self.assertTrue(any(a["path"].endswith("student/notes.json") for a in public))
        self.assertFalse(any(a["path"].endswith(("key.json","score.py")) for a in public))
        self.assertTrue(any(a["path"] == "teacher/exam/key.json" and a["visibility"] == "teacher"
                            for a in activity["assets"]))
