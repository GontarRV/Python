import unittest
from Bidirectional_linked_list_dummy import Node, LinkedList2

class TestsLinkedList2(unittest.TestCase):

    def test_add_in_tail(self):
        list1 = LinkedList2()
        self.assertEqual(list1.len(), 0)
        list1.add_in_tail(Node(8))
        self.assertEqual(list1.len(), 1)
        self.assertEqual(list1.head.next.value, 8)
        self.assertEqual(list1.tail.prev.value, 8)
        list1.add_in_tail(Node(55))
        self.assertEqual(list1.len(), 2)
        self.assertEqual(list1.head.next.value, 8)
        self.assertEqual(list1.tail.prev.value, 55)

    def test_len(self):
        list1 = LinkedList2()
        self.assertEqual(list1.len(), 0)
        list1.add_in_head(Node(12))
        list1.add_in_tail(Node(55))
        self.assertEqual(list1.len(), 2)
        list1.delete(12)
        self.assertEqual(list1.len(), 1)

    def test_clean(self):
        list1 = LinkedList2()
        list1.add_in_head(Node(12))
        list1.add_in_tail(Node(55))
        list1.clean()
        self.assertIsNone(list1.head.value)
        self.assertIsNone(list1.tail.value)
        self.assertEqual(list1.len(), 0)

    def test_add_in_head(self):
        list1 = LinkedList2()
        list1.add_in_head(Node(12))
        self.assertEqual(list1.head.next.value, 12)
        self.assertEqual(list1.tail.prev.value, 12)
        list1.add_in_head(Node(55))
        self.assertEqual(list1.head.next.value, 55)
        self.assertEqual(list1.tail.prev.value, 12)

    def test_find(self):
        list1 = LinkedList2()
        self.assertIsNone(list1.find(Node(15)))
        list1.add_in_tail(Node(12))
        list1.add_in_tail(Node(55))
        list1.add_in_tail(Node(128))
        self.assertEqual(list1.find(55).value, 55)

    def test_find_all(self):
        list1 = LinkedList2()
        self.assertEqual(list1.find_all(12), [])
        list1.add_in_tail(Node(12))
        list1.add_in_tail(Node(55))
        list1.add_in_tail(Node(128))
        list1.add_in_tail(Node(55))
        list1.add_in_tail(Node(55))
        list1.add_in_tail(Node(55))
        result = [node.value for node in list1.find_all(55)]
        self.assertEqual(result, [55, 55, 55, 55])

    def test_delete(self):
        list1 = LinkedList2()
        list1.delete(55, all=False)
        self.assertEqual(list1.head.next.value, None)
        self.assertEqual(list1.tail.prev.value, None)
        list1.add_in_tail(Node(12))
        list1.add_in_tail(Node(55))
        list1.add_in_tail(Node(128))
        list1.delete(55, all=False)
        self.assertEqual(list1.head.next.value, 12)
        self.assertEqual(list1.tail.prev.value, 128)
        list1.add_in_tail(Node(12))
        list1.add_in_tail(Node(55))
        list1.add_in_tail(Node(128))
        list1.delete(128, all=True)
        self.assertEqual(list1.head.next.value, 12)
        self.assertEqual(list1.tail.prev.value, 55)

    def test_insert(self):
        list1 = LinkedList2()
        list1.insert(None, Node(12))
        self.assertEqual(list1.head.next.value, 12)
        self.assertEqual(list1.tail.prev.value, 12)
        list1.insert(None, Node(128))
        self.assertEqual(list1.head.next.value, 12)
        self.assertEqual(list1.tail.prev.value, 128)

if __name__ == '__main__':
    unittest.main()

    