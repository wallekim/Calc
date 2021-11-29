import unittest
from src import separator


class TestSeparator(unittest.TestCase):
    def test_split(self):
        self.assertEqual(separator.split_('1+1'), ['1', '+', '1'])
        self.assertEqual(separator.split_('  1  +  1   '), ['1', '+', '1'])
        self.assertEqual(separator.split_('(((1)))'), ['(', '(', '(', '1', ')', ')', ')'])

        self.assertRaises(BaseException, separator.split_('sadfsd'))