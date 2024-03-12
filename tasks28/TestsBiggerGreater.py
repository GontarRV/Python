import unittest
from BiggerGreater import BiggerGreater

class TestsBiggerGreater(unittest.TestCase):

    def tests_one(self):
        self.assertEqual(BiggerGreater('ая'), 'яа')

    def tests_two(self):
        self.assertEqual(BiggerGreater('fff'), '')

    def tests_three(self):
        self.assertEqual(BiggerGreater('нклм'), 'нкмл')

    def tests_four(self):
        self.assertEqual(BiggerGreater('вибк'), 'викб')

    def tests_five(self):
        self.assertEqual(BiggerGreater('вкиб'), 'ибвк')

if __name__ = '__main__':
    unittest.main()

    