import unittest
from src import notation


class TestCalc(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(notation.transformation(['1', '+', '1']), ['1', '1', '+'])
        self.assertEqual(notation.transformation(['+', '111', '+', '111']), ['111', '+', '111', '+'])
        self.assertEqual(notation.transformation(['22', '+', '13', '+', '2', '+', '87']), ['22', '13', '+', '2', '+', '87', '+'])

    def test_minus(self):
        self.assertEqual(notation.transformation(['1', '-', '1']), ['1', '1', '-'])
        self.assertEqual(notation.transformation(['111', '-', '111']), ['111', '111', '-'])
        self.assertEqual(notation.transformation(['-', '1', '-', '1']), ['1', '-',  '1', '-'])

    def test_division(self):
        self.assertEqual(notation.transformation(['15', '/', '15']), ['15', '15', '/'])
        self.assertEqual(notation.transformation(['1', '/', '2']), ['1', '2', '/'])

    def test_multiple(self):
        self.assertEqual(notation.transformation(['1', '*', '2']), ['1', '2', '*'])
        self.assertEqual(notation.transformation(['1', '*', '2', '*', '3', '*', '4']),
                         ['1', '2', '*', '3', '*', '4', '*'])

    def test_brackets(self):
        test_in = '( 1 + 2 )'.split()
        self.assertEqual(notation.transformation(test_in), ['1', '2', '+'])
        test_in = '( 2 - 2 + ( 1 + 2 ) + 3 - 4 )'.split()
        self.assertEqual(notation.transformation(test_in), ['2', '2', '-', '1', '2', '+', '+', '3', '+', '4', '-'])

    def test_hard(self):
        test_in = '( 1 + 2 ) * 4 + 3'.split()
        self.assertEqual(notation.transformation(test_in),
            ['1', '2', '+', '4', '*', '3', '+'])

        test_in = '( 1 + 5 ) * 4 + ( 2 - 4 ) * 3'.split()
        self.assertEqual(
            notation.transformation(test_in), ['1', '5', '+', '4', '*', '2', '4', '-', '3', '*', '+'])

        test_in = '( ( 3 + 2 ) * 3 + 5 - 3 ) * 4 + 2'.split()
        self.assertEqual((notation.transformation(test_in)),
                         ['3', '2', '+', '3', '*', '5', '+', '3', '-', '4', '*', '2', '+'])

        test_in = '( 4 + ( 3 + 2 ) * 3 + 5 - 3 ) * 4 + 2'.split()
        self.assertEqual(notation.transformation(test_in),
            ['4', '3', '2', '+', '3', '*', '+', '5', '+', '3', '-', '4', '*', '2', '+'])

        test_in = '( 4 + ( 3 + 2 ) * 3 + 5 - 3 ) / 4 + 2'.split()
        self.assertEqual(notation.transformation(test_in),
            ['4', '3', '2', '+', '3', '*', '+', '5', '+', '3', '-', '4', '/', '2', '+'])

        test_in = '( 4 + ( 3 + 2 ) * 3 + 5 - 3 ) / ( 4 + 2 )'.split()
        self.assertEqual(notation.transformation(test_in),
            ['4', '3', '2', '+', '3', '*', '+', '5', '+', '3', '-', '4', '2', '+', '/'])