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

    def test_count(self):
        """ testing that 'count' works the way you think """
        word = "word   wordwordword word w ord   "
        self.assertEqual(5, word.count('word'), "test that 'count' works")
        self.assertEqual(1, word.count('word', 20), "test that 'count' works ")
        self.assertEqual(1, word.count('word', 6, 12), "test that 'count' works")

    def test_endswith(self):
        """ testing that 'endswith' works the way you think """
        sentence = "this is the thing"
        sentence2 = "this is the other thing yo"
        self.assertTrue(sentence.endswith("thing"), "test that endswith works")
        self.assertFalse(sentence2.endswith("thing"), "test that endswith works")


if __name__ == '__main__':
    unittest.main()
