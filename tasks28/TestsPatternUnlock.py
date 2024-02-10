import unittest
from PatternUnlock import PatternUnlock

class PatternUnlockTests(unittest.TestCase):

    def tests_mini(self):
        self.assertEqual(PatternUnlock(3, [9, 2, 4]), '282843')

    def tests_maxi(self):
        self.assertEqual(PatternUnlock(15, [6, 1, 9, 8, 7, 2, 6, 5, 4, 3, 7, 8, 2, 5, 1]), '1524264')

if __name__ == '__main__':
    unittest.main()