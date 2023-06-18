import unittest
from translator import englishToFrench, frenchToEnglish

class TranslatorTestCase(unittest.TestCase):
    def test_english_to_french(self):
        result = englishToFrench("Hello")
        self.assertEqual(result, "Bonjour")

        result = englishToFrench("Goodbye")
        self.assertEqual(result, "Au revoir")

    def test_french_to_english(self):
        result = frenchToEnglish("Bonjour")
        self.assertEqual(result, "Hello")

        
        result = frenchToEnglish("Au revoir")
        self.assertEqual(result, "Goodbye")

if __name__ == '__main__':
    unittest.main()