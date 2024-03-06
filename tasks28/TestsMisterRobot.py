import unittest
from MisterRobot import MisterRobot

class TestsMisterRobot(unittest.TestCase):

    def tests_one(self):
        self.assertEqual(MisterRobot(7, [1,3,4,5,6,2,7]), True)

    def tests_two(self):
        self.assertEqual(MisterRobot(7, [7,3,4,5,6,2,1]), False)

    def tests_three(self):
        self.assertEqual(MisterRobot(5, [5,3,4,1,2]), True)

    def tests_four(self):
        self.assertEqual(MisterRobot(10, [10,8,9,1,3,4,5,6,2,7]), False)

if __name__ == '__main__':
    unittest.main()