import unittest
from calculator import double


class CalculatorTests(unittest.TestCase):
    def test_double(self):
        self.assertEqual(double(3), 6)
