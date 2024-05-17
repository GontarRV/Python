import unittest
from OrderedList import OrderedList


class TestOrderedList(unittest.TestCase):
    def test_compare(self):
        orlist = OrderedList(True)
        self.assertEqual(-1, orlist.compare(100, 200))
        self.assertEqual(1, orlist.compare(100, 49))
        self.assertEqual(0, orlist.compare(100, 100))

    def test_add(self):
        orlist = OrderedList(True)
        self.assertEqual(0, orlist.len())
        orlist.add(10)
        self.assertEqual(1, orlist.len())
        self.assertIsNone(orlist.head.prev)
        self.assertIsNone(orlist.tail.next)
        orlist.add(20)
        self.assertEqual(2, orlist.len())
        self.assertEqual(20, orlist.head.next.value)
        self.assertIsNone(orlist.head.prev)
        self.assertIsNone(orlist.tail.next)
        orlist.add(30)
        self.assertEqual(3, orlist.len())
        self.assertEqual(10, orlist.head.value)
        self.assertEqual(30, orlist.tail.value)

        orlist1 = OrderedList(False)
        self.assertEqual(0, orlist1.len())
        orlist1.add(10)
        self.assertEqual(1, orlist1.len())
        self.assertIsNone(orlist1.head.prev)
        self.assertIsNone(orlist1.tail.next)
        orlist1.add(20)
        self.assertEqual(10, orlist1.head.next.value)
        self.assertIsNone(orlist1.head.prev)
        self.assertIsNone(orlist1.tail.next)
        self.assertEqual(2, orlist1.len())
        30, orlist1.add(30)
        self.assertEqual(3, orlist1.len())
        self.assertEqual(30, orlist1.head.value)
        self.assertEqual(10, orlist1.tail.value)

    def test_find(self):
        orlist = OrderedList(True)
        for i in range(100):
            orlist.add(i)
        self.assertIsNone(orlist.find(-1))
        self.assertIsNone(orlist.find(101))
        self.assertEqual(0, orlist.find(0).value)
        self.assertEqual(49, orlist.find(49).value)
        self.assertEqual(99, orlist.find(99).value)
        self.assertIsNone(orlist.find(100))

        orlist1 = OrderedList(False)
        for i in range(100):
            orlist1.add(i)
        self.assertIsNone(orlist.find(-1))
        self.assertIsNone(orlist.find(101))
        self.assertEqual(0, orlist.find(0).value)
        self.assertEqual(49, orlist.find(49).value)
        self.assertEqual(99, orlist.find(99).value)
        self.assertIsNone(orlist.find(100))

    def test_delete(self):
        orlist = OrderedList(True)
        for i in range(100):
            orlist.add(i)
        self.assertIsNone(orlist.delete(-1))
        self.assertIsNone(orlist.delete(101))
        self.assertIsNone(orlist.delete(100))
        orlist.delete(0)
        self.assertIsNone(orlist.delete(0))
        orlist.delete(99)
        self.assertIsNone(orlist.delete(99))
        orlist.delete(49)
        self.assertIsNone(orlist.delete(49))
        self.assertEqual(49, orlist.add(49))
        self.assertEqual(49, orlist.add(49))
        self.assertEqual(49, orlist.delete(49))
        self.assertEqual(49, orlist.delete(49))
        self.assertIsNone(orlist.delete(49))

        for j in range(orlist.len()):
            if j == 96:
                None
            self.assertEqual(orlist.head.value, orlist.delete(orlist.head.value))
        self.assertEqual(0, orlist.len())
        self.assertIsNone(orlist.delete(10))

    def test_clean(self):
        orlist = OrderedList(True)
        for i in range(100):
            orlist.add(i)
        self.assertEqual(100, orlist.len())

        self.assertIsNone(orlist.clean(False))
        self.assertEqual(0, orlist.len())
        for i in range(100):
            orlist.add(i)
        self.assertEqual(99, orlist.head.value)
        self.assertEqual(0, orlist.tail.value)

    def test_len(self):
        orlist = OrderedList(True)
        self.assertEqual(0, orlist.len())
        for i in range(50):
            self.assertEqual(i, orlist.add(i))
            self.assertEqual(i + 1, orlist.len())

        orlist.clean(True)
        for i in range(50):
            self.assertEqual(i, orlist.add(i))
            self.assertEqual(i + 1, orlist.len())

    def test_get_all(self):
        orlist = OrderedList(True)
        self.assertEqual(0, orlist.len())
        self.assertEqual([], orlist.get_all())
        for i in range(100):
            orlist.add(i)
        self.assertEqual(100, orlist.len())

        orlist1 = OrderedList(False)
        self.assertEqual(0, orlist1.len())
        self.assertEqual([], orlist1.get_all())
        for i in range(100):
            orlist1.add(i)
        self.assertEqual(100, orlist1.len())

if __name__ == "__main__":
    unittest.main()