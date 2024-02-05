import squirrel
import unittest

class squirrelTests(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(squirrel.squirrel(0), 1)

    def test_a_large_number(self):
        self.assertEqual(squirrel.squirrel(10000), 2)

if __name__ == '__main__':
    unittest.main()