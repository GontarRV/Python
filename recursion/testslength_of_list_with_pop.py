import unittest
from length_of_list_with_pop import length_of_list_with_pop

class Testslenght_of_list_with_pop(unittest.TestCase):

    def testlenght_of_list_with_pop(self):
        self.assertEqual(length_of_list_with_pop([]), 0)
        self.assertEqual(length_of_list_with_pop([1, 1, 1, 1]), 4)
        self.assertEqual(length_of_list_with_pop([2, 2, 2, 2, 2, 2, 2]), 7)
        self.assertEqual(length_of_list_with_pop([3, 3, 3, 3, 3, 3, 3, 3, 3, 3]), 10)

if __name__ == '__main__':
    unittest.main()