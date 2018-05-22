""" module for testing string builtin """
import unittest

class MyStringTest(unittest.TestCase):
    """ testing that str builtin works they way you think """

    def test_capitalize(self):
        """ testing that 'capitalize' works the way you think """
        word = "word"
        self.assertEqual('Word', word.capitalize(), "test that capitalize function works")

    def test_casefold(self):
        """ testing that 'casefold' works the way you think """
        word = "WORD"
        self.assertEqual('word', word.casefold(), "test that casefold function works")

    def test_center(self):
        """ testing that 'center' works the way you think """
        word = "word"
        self.assertEqual("   word   ", word.center(10), "test that 'center' works")
        self.assertEqual("___word___", word.center(10, '_'), "test that 'center' works with fill")

if __name__ == '__main__':
    unittest.main()
