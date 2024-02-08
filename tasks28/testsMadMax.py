import unittest
import MadMax

class MadMaxTests(unittest.TestCase):

    def tests_one(self):
        self.assertEqual(MadMax.MadMax(1, 1), 1)

    def tests_nine(self):
        self.assertEqual(MadMax.MadMax(9, [1,9,3,5,2,6,4,8,7]), [1,2,3,4,9,8,7,6,5])

if __name__ == '__main__':
    unittest.main()