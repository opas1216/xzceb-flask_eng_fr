import unittest
from translator import frenchToEnglish, englishToFrench


class TestTranslator(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish(""), "")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Bonjour")

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench(""), "")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertNotEqual(englishToFrench("Hello"), "Hello")

unittest.main()