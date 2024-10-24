import unittest
from find_second_max_num import find_second_max_num

class Tests_find_second_max_num(unittest.TestCase):
    def tests_find_second_max_num(self):
        self.assertEqual(find_second_max_num([0, 1, 2, 3, 4]), 3)
        self.assertEqual(find_second_max_num([0, 4, 2, 3, 4]), 4)
        self.assertEqual(find_second_max_num([1, 3, 2, 3, 4]), 3)
        self.assertEqual(find_second_max_num([5, 1, 2, 3, 4]), 4)
        self.assertEqual(find_second_max_num([0, 1, 2, 1, 4]), 2)
        self.assertEqual(find_second_max_num([1, 2, 2, 2, 4]), 2)
        self.assertEqual(find_second_max_num([4, 6, 2, 3, 4]), 4)
        self.assertEqual(find_second_max_num([5, 7, 2, 3, 4]), 5)
        self.assertEqual(find_second_max_num([7, 5, 2, 3, 4]), 5)

if __name__ = '__main__':
    unittest.main()