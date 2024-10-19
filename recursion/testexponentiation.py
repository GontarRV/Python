import unittest
import exponentiation

class exponentiationTests(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(exponentiation.exponentiation(100, 0), 1)
        self.assertEqual(exponentiation.exponentiation(100000, 0), 1)

    def test_min_number(self):
        self.assertEqual(exponentiation.exponentiation(1, 10000), 1)
        self.assertEqual(exponentiation.exponentiation(10, 3), 1000)

    def test_max_number(self):
        self.assertEqual(exponentiation.exponentiation(100, 10), 100000000000000000000)
    
if __name__ == '__main__':
    unittest.main()