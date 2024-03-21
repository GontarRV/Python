import unittest
from white_walkers import white_walkers

class Testswhite_walkers(unittest.TestCase):

    def tests_one(self):
        self.assertEqual(white_walkers("axxb6===4xaf5===eee5"), True)

    def tests_two(self):
        self.assertEqual(white_walkers("5==ooooooo=5=5"), False)

    def tests_three(self):
        self.assertEqual(white_walkers("axxb6===4xaf5===eee5"), True)

    def tests_four(self):
        self.assertEqual(white_walkers("aaS=8"), False)

    def tests_five(self):
        self.assertEqual(white_walkers("9===1===9===1===9"), True)

if __name__ == '__main__':
    unittest.main()