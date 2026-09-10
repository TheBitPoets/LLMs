import io
import json
import unittest
from unittest.mock import patch
from labs.ai_software.proposal import parse_proposal, propose


class ProposalChecks(unittest.TestCase):
    def test_valid_draft(self):
        self.assertEqual(parse_proposal('{"room":"LAB-A","start":540,"end":600}')
                         ["start"], 540)

    def test_invalid_drafts(self):
        for content in ['[]', '{}', 'not json',
                        '{"room":"LAB-A","start":true,"end":600}',
                        '{"room":"LAB-A","start":600,"end":540}',
                        '{"room":"LAB-A","start":480,"end":900}',
                        '{"room":"LAB-C","start":540,"end":600}',
                        '{"room":"LAB-A","start":540,"end":600,"extra":1}',
                        '{"room":"LAB-A","start":540,"end":600,"end":650}']:
            with self.subTest(content=content), self.assertRaises(ValueError):
                parse_proposal(content)

    def test_mocked_request_is_local_and_returns_only_draft(self):
        payload = {"model": "fake-for-test", "message": {"content":
                   '{"room":"LAB-A","start":540,"end":600}'}}
        with patch("urllib.request.urlopen", return_value=io.BytesIO(
                json.dumps(payload).encode())) as request:
            result = propose("fake-for-test", "LAB-A dalle 9 alle 10")
        self.assertEqual(result["status"], "draft_requires_review")
        sent = request.call_args.args[0]
        self.assertEqual(sent.full_url, "http://127.0.0.1:11434/api/chat")
        self.assertFalse(json.loads(sent.data)["stream"])
        self.assertIsNone(result["total_duration_ns"])
