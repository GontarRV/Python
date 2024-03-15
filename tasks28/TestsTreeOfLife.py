import unittest
from TreeOfLife import TreeOfLife

class TestsTreeOfLife(unittest.TestCase):

    def tests_one(self):
        self.assertEqual(TreeOfLife(3, 4, 12, [".+..","..+.",".+.."]), ['.+..', '..+.', '.+..'])

    def tests_two(self):
        self.assertEqual(TreeOfLife(4, 5, 10, ['...+.', '+....', '+....', '..+..']), ['.+...', '..+.+', '...++', '....+'])

if __name__ == '__main__':
    unittest.main()