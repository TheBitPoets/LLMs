"""Regression: handbook commands must match the actual CLI, including args."""
from pathlib import Path
import re
import shlex
import unittest
from labs.course_lab import parser


class DocumentedCommands(unittest.TestCase):
    def test_module_commands_parse(self):
        root = Path(__file__).resolve().parents[1]
        count = 0
        for path in sorted((root / "docs/course/modules").glob("M??-*.md")):
            for command in re.findall(r"`(python3 labs/course_lab\.py [^`]+)`", path.read_text()):
                with self.subTest(module=path.name, command=command):
                    parser().parse_args(shlex.split(command)[2:])
                    count += 1
        self.assertGreater(count, 10, "extraction must cover the handbook CLI examples")
