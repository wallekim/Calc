import unittest
from src import calculating


class TestCalc(unittest.TestCase):
    def test_plus(self):
        test_in = '1 2 + 4 * 3 +'.split()                       # (1 + 2) * 4 + 3
        self.assertEqual(calculating.calculate(test_in), 15)

        test_in = '11 11 +'.split()                             # 11 + 11
        self.assertEqual(calculating.calculate(test_in), 22)

    def test_minus(self):
        test_in = '20 56 -'.split()                             # 20 - 56
        self.assertEqual(calculating.calculate(test_in), -36)

        test_in = '2 5 - 4 - 1 - 5 -'.split()                   # 2-5-4-1-5
        self.assertEqual(calculating.calculate(test_in), -13)

        test_in = '3 0 4 - *'.split()
        self.assertEqual(calculating.calculate(test_in), -12)   # 3 * (-4)

    def test_division(self):
        self.assertEqual(calculating.calculate(['1', '2', '/']), 0.5)

        test_in = '1 2 / 3 / 4 /'.split()                      # 1/2/3/4
        self.assertEqual(calculating.calculate(test_in), 0.041666666666666664)

    def test_multiple(self):
        self.assertEqual(calculating.calculate(['3', '15', '*']), 45)

        test_in = '1 2 * 3 * 4 * 5 *'

    def test_hard(self):
        test_in = '1 5 + 4 * 2 4 - 3 * +'                       # (1 + 5) * 4 + (2 - 4) * 3
        self.assertEqual(calculating.calculate(test_in), 18)

        test_in = '3 2 + 3 * 5 + 3 - 4 * 2 +'.split()           # ((3 + 2) * 3 + 5 - 3) * 4 + 2
        self.assertEqual(calculating.calculate(test_in), 70)
