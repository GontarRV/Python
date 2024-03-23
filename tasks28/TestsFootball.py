import unittest
from Football import Football

class TestsFootball(unittest.TestCase):

    def tests_one(self):
        self.assertEqual(Football([1, 3, 2], 3), True)

    def tests_two(self):
        self.assertEqual(Football([1, 7, 5, 3, 9], 5), True)

    def tests_three(self):
        self.assertEqual(Football([3, 2, 1], 3), True)

    def tests_four(self):
        self.assertEqual(Football([9, 5, 3, 7, 1], 5), False)

    def tests_five(self):
        self.assertEqual(Football([1, 4, 3, 2, 5], 5), True)

if __name__ == '__main__':
    unittest.main()