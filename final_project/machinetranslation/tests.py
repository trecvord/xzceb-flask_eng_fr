import unittest
from translator import english_to_french, french_to_english

class TranslationTests(unittest.TestCase):
    def test_english_to_french(self):
        result = english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')

        result = english_to_french('Bonjour')
        self.assertEqual(result, 'Bonjour')  

    def test_french_to_english(self):
        result = french_to_english('Hello')
        self.assertEqual(result, 'Hello')  

        result = french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')

if __name__ == '__main__':
    unittest.main()