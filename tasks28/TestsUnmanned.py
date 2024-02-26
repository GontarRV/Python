import unittest
from Unmanned import Unmanned

class TestsUnmanned(unittest.TestCase):

    def tests_basic(self):
        self.assertEquaal(Unmanned(10, 2, [[3, 5, 5], [5, 2, 2]]), 12)

    def tests_advanced(self):
        self.assertEqual(Unmanned(15, 3, [[3, 5, 5], [5, 4, 4], [10, 3, 3]]), 20)

    def tests_lots_of_traffic_lights(self):
        self.assertEqual(Unmanned(11, 5, [[2, 5, 5], [3, 3, 3], [5, 2, 2], [7, 4, 4], [9, 3, 3]]), 17)

if __name__ == '__main__':
    unittest.main()