import unittest
import odometer

class odometerTests(unittest.TestCase):

    def test_one(self):
        self.assertEqual(odometer.odometer([1, 1]), 1)

    def test_big_list(self):
        self.assertEqual(odometer.odometer([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), 15)

    def test_the_highest_values(self):
        self.assertEqual(odometer.odometer([10, 1, 1000, 3]), 2010)

if __name__ == '__main__':
    unittest.main()