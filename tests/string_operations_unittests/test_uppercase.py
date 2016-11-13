"""This module aims to test the uppercase method."""


import unittest


class Upper(unittest.TestCase):

    def test_upper_existence(self):
        self.Upper = Upper("aaaa")

    def test_uppercase_null(self):
        with self.assertRaises(IndexError):
            Upper(None)

    def test_uppercase_null(self):
        with self.assertRaises(IndexError):
            Upper("")

    def test_uppercase_null(self):
        with self.assertRaises(TypeError):
            Upper("!23~")

    def test_uppercase_lower_value(self):
        text = "aaaa"
        actual = Upper(text)
        expected = "AAAA"
        self.assertEqual(actual, expected)

    def test_uppercase_upper_value(self):
        text = "AAAA"
        actual = Upper(text)
        expected = "AAAA"
        self.assertEqual(actual, expected)

    def test_uppercase_upper_value(self):
        text = "1anDv"
        actual = Upper(text)
        expected = "1ANDV"
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
