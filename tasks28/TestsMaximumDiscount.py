import unittest
from MaximumDiscount import MaximumDiscount

class TestsMaximumDiscort(unittest.TestCase):

    def tests_basic(self):
        self.assertEqual(MaximumDiscount(7, [400, 350, 300, 250, 200, 150, 100]), 450)
    
    def tests_the_same_pair(self):
        self.assertEqual(MaximumDiscount(11, [400, 1000, 1500, 50, 1000, 350, 300, 250, 200, 150, 100]), 1450)
    
    def tests_all_at_the_same_price(self):
        self.assertEqual(MaximumDiscount(8, [100, 100, 100, 100, 100, 100, 100, 100]), 200)

if __name__ == '__main__':
    unittest.main()