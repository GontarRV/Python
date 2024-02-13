import unittest
from SumOfThe import SumOfThe

class SumOfTheTests(unittest.TestCase):

    def tests_an_example(self):
        self.assertEqual(SumOfThe(7, [100, -50, 10, -25, 90, -35, 90]), 90)

    def tests_arbitrary(self):
        self.assertEqual(SumOfThe(5, [150, -50, 100, -30, 30]), 100)

    def tests_large_numbers(self):
        self.assertEqual(SumOfThe(6, [100000, -70000, -30000,
                                      20000, -10000, 10000]), 10000)

    def tests_lots_of_numbers(self):
        self.assertEqual(SumOfThe(19, [9, -9, -8, -7, 1, 2, -6, -5,
                                       -4, 3, 4, -3, -2, 5, 6, 7,
                                       -1, 0, 8]), 0)

if __name__ == '__main__':
    unittest.main()