import unittest
from WordSearch import WordSearch

class WordSearchTests(unittest.TestCase):

    def tests_eng(self):
        self.assertEqual(WordSearch(5, 'a line of text to check the task', 'text'), [0,0,0,1,0,0,0,0])

    def tests_none(self):
        self.assertEqual(WordSearch(5, 'a line of text to check the task', 'taxi'), [0,0,0,0,0,0,0,0])

    def tests_big_word(self):
        self.assertEqual(WordSearch(6, 'просто набор слов параллепипед и параллелограмм', 'слов'), [0,0,1,0,0,0,0,0,0])

if __name__ == '__main__':
    unittest.main()