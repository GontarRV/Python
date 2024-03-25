import unittest
from Keymaker import Keymaker

class TestsKeymaker(unittest.TestCase):

    def tests_one(self):
        self.assertEqual(Keymaker(1), '1')

    def tests_two(self):
        self.assertEqual(Keymaker(4), '1001')

    def tests_three(self):
        self.assertEqual(Keymaker(8), '10010000')

if __name__ == '__main__':
    unittest.main()