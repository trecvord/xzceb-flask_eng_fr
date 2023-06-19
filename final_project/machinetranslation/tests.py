import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TranslationTests(unittest.TestCase):
    def test_english_to_french_hello(self):
        result = english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')

    def test_english_to_french_goodbye(self):
        result = english_to_french('Goodbye')
        self.assertEqual(result, 'Au revoir')

    def test_french_to_english_bonjour(self):
        result = french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')

    def test_french_to_english_au_revoir(self):
        result = french_to_english('Au revoir')
        self.assertEqual(result, 'Goodbye')

    def test_english_to_french_empty_string(self):
        result = english_to_french('')
        self.assertEqual(result, '')

    def test_french_to_english_empty_string(self):
        result = french_to_english('')
        self.assertEqual(result, '')

if __name__ == '__main__':
    unittest.main()