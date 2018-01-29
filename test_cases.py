import unittest
from main import Wordcount

TEST_FILE = 'test.txt'

class TestStringMethods(unittest.TestCase):

    def test_no_file(self):
        with self.assertRaises(Exception):
            Wordcount().read_file()

    def test_non_exising_file(self):
        with self.assertRaises(FileNotFoundError):
            Wordcount('non_existing_file.txt').read_file()

    def test_file_reader(self):
        word_string = "Stripped-down men's Men's a. A Tradeshift.com challenge."
        word_count_obj = Wordcount(filename=TEST_FILE)
        word_data = word_count_obj.read_file()
        
        self.assertEqual(word_data, word_string)

    def test_file(self):
        word_count = {"stripped-down": 1, "men's": 2, "a": 2, "tradeshift.com": 1, "challenge": 1}
        word_count_obj = Wordcount(filename=TEST_FILE)
        word_data = word_count_obj.read_file()
        word_count_obj.update_word_count(word_data)

        self.assertEqual(word_count_obj.word_cound, word_count)

if __name__ == '__main__':
    unittest.main()