import unittest

from deque_palindrome import Deque

class TestDeque(unittest.TestCase):
    def test1(self):
        deque = Deque()
        self.assertEqual(0, deque.size())
        deque.addFront(2)
        deque.removeFront()
        self.assertEqual(0, deque.size())
        deque.addFront(5)
        deque.removeFront()
        self.assertEqual(0, deque.size())

    def test2(self):
        deque = Deque()
        self.assertEqual(0, deque.size())
        deque.addTail(2)
        deque.removeTail()
        self.assertEqual(0, deque.size())
        deque.addTail(5)
        deque.removeTail()
        self.assertEqual(0, deque.size())

    def test3(self):
        deque = Deque()
        self.assertEqual(0, deque.size())
        deque.addFront(2)
        deque.addFront(5)
        deque.removeFront()
        deque.addTail(7)
        deque.addTail(12)
        deque.removeTail()
        self.assertEqual(2, deque.size())

    def test4(self):
        deque = Deque()
        self.assertEqual(0, deque.size())
        deque.addFront(2)
        deque.addFront(5)
        deque.removeFront()
        deque.addTail(7)
        deque.addTail(12)
        deque.removeTail()
        self.assertEqual(2, deque.size())

    def test5(self):
        deque = Deque()
        self.assertEqual(0, deque.size())
        for value in range(5):
            deque.addTail(value)
            self.assertEqual(value + 1, deque.size())
        for value in range(5):
            deque.addFront(value)
            self.assertEqual(value + 1 + 5, deque.size())
        for value in range(5):
            deque.removeFront()
            deque.removeTail()
        self.assertIsNone(deque.removeTail())
        self.assertIsNone(deque.removeFront())
        self.assertEqual(0, deque.size())

if __name__ == '__main__':
    unittest.main()