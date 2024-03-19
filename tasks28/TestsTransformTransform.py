import unittest
from TransformTransform import TransformTransform

class TestsTransformTransform(unittest.TestCase):

    def tests_one(self):
        self.assertEqual((TransformTransform([1, 2, 3, 4], 4)), False)

    def tests_two(self):
        self.assertEqual(TransformTransform([4, 4, 4, 4], 4), True)

    def tests_three(self):
        self.assertEqual(TransformTransform([9, 8, 7, 6, 5], 5), False)

    def tests_four(self):
        self.assertEqual(TransformTransform([5, 4, 4, 6], 4), True)

if __name__ = '__main__':
    unittest.main()

    