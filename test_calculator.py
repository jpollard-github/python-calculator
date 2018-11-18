from calculator import Calculator

import unittest

class TestCalculator(unittest.TestCase):

    def test_sum1(self):
        calc = Calculator()
        self.assertEqual(calc.sum(1, 2), 3)

    def test_sum2(self):
        calc = Calculator()
        self.assertEqual(calc.sum(-5, 40), 35)

    def test_sum3(self):
        calc = Calculator()
        self.assertEqual(calc.sum(0, 0), 0)

    def test_mult1(self):
        calc = Calculator()
        self.assertEqual(calc.mult(2, 3), 6)

    def test_mult2(self):
        calc = Calculator()
        self.assertEqual(calc.mult(0, 0), 0)

    def test_mult3(self):
        calc = Calculator()
        self.assertEqual(calc.mult(-5, 40), -200)

if __name__ == '__main__':
    unittest.main()
