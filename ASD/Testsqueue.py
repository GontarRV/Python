import unittest

from queue import Queue


class TestQueue(unittest.TestCase):
    def test_constructor(self):
        queue1 = Queue()
        self.assertEqual(queue1.size(), 0)

    def test_enqueue(self):
        queue1 = Queue()
        queue1.enqueue(2)
        self.assertEqual(queue1.size(), 1)
        queue1.enqueue(7)
        self.assertEqual(queue1.size(), 2)

    def test_dequeue(self):
        queue1 = Queue()
        queue1.enqueue(2)
        queue1.enqueue(7)
        queue1.dequeue()
        queue1.dequeue()
        self.assertEqual(queue1.size(), 0)

    def test_size(self):
        queue1 = Queue()
        for value in range(50):
            queue1.enqueue(value)
        self.assertEqual(queue1.size(), 50)


if __name__ == '__main__':
    unittest.main()