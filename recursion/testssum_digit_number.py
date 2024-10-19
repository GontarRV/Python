import unittest
from sum_digit_number import sum_digit_number

class Tests_sum_digit_numbers(unittest.TestCase):

    def tests_one_number(self):
        self.assertEqual(sum_digit_number(9), 9)
        self.assertEqual(sum_digit_number(2), 2)

    def tests_big_digit(self):
        self.assertEqual(sum_digit_number(123456789), 45)

if __name__ == '__main__':
    unittest.main()