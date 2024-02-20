import unittest
from BigMinus import BigMinus

class BigMinusTests(unittest.TestCase):

    def tests_small_nums(self):
        self.assertEqual(BigMinus('12345', '2346'), '9999')

    def tests_big_nums(self):
        self.assertEqual(BigMinus('11000000000000000', '2346'), '10999999999997654')

if __name__ == '__main__':
    unittest.main()

    