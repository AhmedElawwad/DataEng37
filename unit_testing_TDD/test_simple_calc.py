from simple_calc import SimpleCalc
from unittest import TestCase


# python -m unittest    - to run the test in the terminal

class CalcTest(TestCase):
    calc = SimpleCalc()

    def test_add(self):
        actual = self.calc.add(2, 4)
        expected = 6

        self.assertEqual(actual, expected)

    def test_subtract(self):

        actual = self.calc.subtract(5, 3)
        expected = 2

        self.assertEqual(actual, expected)

    def test_multiply(self):

        actual = self.calc.multiply(5, 3)
        expected = 15

        self.assertEqual(actual, expected)

    def test_division(self):

        actual = self.calc.division(15, 3)
        expected = 5

        self.assertEqual(actual, expected)


