"""Run from repository root: python -m unittest discover -s tests."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / "coursework" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class BasicsTest(unittest.TestCase):
    def test_count_fives(self):
        count = load("count_fives", "count_fives.py").count_fives
        self.assertEqual(count(4), 0)
        self.assertEqual(count(15), 2)
        self.assertEqual(count(55), 12)

    def test_game_result(self):
        winner = load("rps", "rock_paper_scissors.py").winner
        self.assertEqual(winner("rock", "scissors"), 1)
        self.assertEqual(winner("rock", "paper"), -1)
        self.assertEqual(winner("rock", "rock"), 0)

    def test_age(self):
        from datetime import date
        calc = load("ages", "age_calculator.py").calculate_age
        self.assertEqual(calc(date(2000, 1, 1), date(2025, 1, 1)), (25, 9132))


if __name__ == "__main__":
    unittest.main()
