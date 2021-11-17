import unittest
from src import calculating


class TestCalc(unittest.TestCase):
    def test_calculating(self):
        self.assertEqual(calculating.calculate(['1', '2', '+', '4', '*', '3', '+']), 15)
        self.assertEqual(calculating.calculate(['1', '5', '+', '4', '*', '2', '4', '-', '3', '*', '+']), 18)
        self.assertEqual(calculating.calculate(['3', '2', '+', '3', '*', '5', '+', '3', '-', '4', '*', '2', '+']), 70)


a = TestCalc()
a.test_polsky()
a.test_calculating()