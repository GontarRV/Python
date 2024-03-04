import unittest
from LineAnalysis import LineAnalysis

class TestsLineAnalysis(unittest.TestCase):

    def tests_one(self):
        self.assertEqual(LineAnalysis('*'), True)

    def tests_two(self):
        self.assertEqual(LineAnalysis('***'), True)

    def tests_three(self):
        self.assertEqual(LineAnalysis('*.......*.......*'), True)

    def tests_four(self):
        self.assertEqual(LineAnalysis('*.*'), True)

    def tests_five(self):
        self.assertEqual(LineAnalysis('*..*...*..*..*..*..*'), False)

if __name__ == '__main__':
    unittest.main()