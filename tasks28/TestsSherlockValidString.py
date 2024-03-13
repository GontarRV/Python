import unittest
from SherlockValidString import SherlockValidString

class TestsSherlockValidString(unittest.TastCase):

    def tests_one(self):
        self.assertEqual(SherlockValidString('xxyyzabc'), False)

    def tests_two(self):
        self.assertEqual(SherlockValidString('xxyyza'), False)

    def tests_three(self):
        self.assertEqual(SherlockValidString('xyzzz'), False)

    def tests_four(self):
        self.assertEqual(SherlockValidString('xxyyz'), True)

    def tests_five(self):
        self.assertEqual(SherlockValidString('xyzaa'), True)

    def tests_six(self):
        self.assertEqual(SherlockValidString('xyz'), True)

if __name__ == '__main__':
    unittest.main()