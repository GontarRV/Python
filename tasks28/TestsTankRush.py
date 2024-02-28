import unittest
from TankRush import TankRush

class TestsTankRush(unittest.TestCase):

    def tests_one(self):
        self.assertEqual(TankRush(3, 4, '1234 2345 0987', 2, 2, '34 98'), True)
    
    def tests_two(self):
        self.assertEqual(TankRush(3, 4, '1234 2534 0798', 2, 2, '34 98'), True)

    def tests_three(self):
        self.assertEqual(TankRush(3, 4, '1234 3425 0987', 2, 2, '34 98'), False)

    def tests_four(self):
        self.assertEqual(TankRush(3, 4, '1234 2345 0977', 2, 2, '34 98'), False)

    def tests_five(self):
        self.assertEqual(TankRush(3, 4, '1234 2345 0987', 4, 2, '34 98 75 54'), False)

    def tests_six(self):
        self.assertEqual(TankRush(3, 4, '1344 2235 0987', 2, 2, '34 98'), False)
    
if __name__ == '__main__':
    unittest.main()