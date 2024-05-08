import unittest
from Stack import Stack
from Stack import balance


class TestStack(unittest.TestCase):
    def test_size(self):
        stack = Stack()
        stack.push(5)
        stack.push(7)
        stack.push(12)
        stack.push(13)
        stack.push(17)
        self.assertEqual(5, stack.size())

    def test_pop(self):
        stack = Stack()
        self.assertIsNone(stack.pop())
        stack.push(5)
        stack.push(7)
        stack.push(12)
        stack.push(13)
        stack.push(17)
        self.assertEqual(17, stack.pop())


    def test_push(self):
        stack = Stack()
        self.assertEqual(5, stack.push(5))
        self.assertEqual(7, stack.push(7))
        self.assertEqual(12, stack.push(12))
        self.assertEqual(13, stack.push(13))
        self.assertEqual(17, stack.push(17))
        self.assertEqual(5, stack.size())
        self.assertEqual(17, stack.stack[0])
        self.assertEqual(5, stack.stack[-1])

    def test_peek(self):
        stack = Stack()
        self.assertIsNone(stack.peek())
        stack.push(5)
        self.assertEqual(5, stack.peek())
        stack.push(7)
        self.assertEqual(7, stack.peek())

    def test_balance(self):
        self.assertTrue(balance("()"))
        self.assertTrue(balance("(()((())()))"))
        self.assertTrue(balance("(()()())"))
        self.assertTrue(balance(""))
        self.assertFalse(balance("("))
        self.assertFalse(balance(")())"))
        self.assertFalse(balance("())("))
        self.assertFalse(balance("(()()(()"))
        self.assertFalse(balance("((())"))


if __name__ == '__main__':
    unittest.main()