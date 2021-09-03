import unittest
from baymax_basic_operations.baymax_calculate import BaymaxCalculate


class TestBaymaxCalculations(unittest.TestCase):
    def setUp(self) -> None:
        self.baymax_calculator = BaymaxCalculate()

    def test_baymax_addition(self):
        baymax_add = self.baymax_calculator.add('500 + 500')
        self.assertEqual(1000, baymax_add)

    def test_baymax_subtraction(self):
        baymax_minus = self.baymax_calculator.subtract('500 - 500')
        self.assertEqual(0, baymax_minus)

    def test_baymax_multplication(self):
        baymax_multiply = self.baymax_calculator.multiplication('5 * 5')
        self.assertEqual(25, baymax_multiply)

    def test_baymax_division(self):
        baymax_divide = self.baymax_calculator.divide('25 / 5')
        self.assertEqual(5, baymax_divide)
