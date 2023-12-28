import unittest
from sorting_an_array import sorting

class SortingTests(unittest.TestCase):

    def test_work_minus(self):
        list1 = [-1, -6, -3, -2, -4, -5, -9, -7, -8]
        list2 = [-9, -8, -7, -6, -5, -4, -3, -2, -1]
        sorting(list1)
        self.assertEqual(list1, list2)

    def test_null(self):
        list1 = []
        list2 = []
        sorting(list1)
        self.assertEqual(list1, list2)
    
    def test_work_plus(self):
        list1 = [1, 3, 4, 7, 9, 8, 2, 5, 6]
        list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sorting(list1)
        self.assertEqual(list1, list2)

    def test_work_with_two_identical_values(self):
        list1 = [-1, -5, -4, 0, 2, 5, 2, 7]
        list2 = [-5, -4, -1, 0, 2, 2, 5, 7]
        sorting(list1)
        self.assertEqual(list1, list2) 

if __name__ == '__main__':
    unittest.main()