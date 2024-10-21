import unittest
from palindrome import palindrome


class Test(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(palindrome(""), True)
        self.assertEqual(palindrome("0"), True)
        self.assertEqual(palindrome("11"), True)
        self.assertEqual(palindrome("23"), False)
        self.assertEqual(palindrome("332"), False)
        self.assertEqual(palindrome("232"), True)
        self.assertEqual(palindrome("2123"), False)
        self.assertEqual(palindrome("32123"), True)
        self.assertEqual(palindrome("32 123"), False)
        self.assertEqual(palindrome("32143"), False)
        self.assertEqual(palindrome("31 23"), False)
        self.assertEqual(palindrome("34 43"), True)

if __name__ == '__main__':
    unittest.main()