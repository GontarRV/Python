import unittest
from Bidirectional_linked_list import Node, LinkedList2

def list_linkedlist(l):
    result = []
    node = l.head
    while node is not None:
        result.append(node.value)
        node = node.next
    return result

class TestLinkedList(unittest.TestCase):

    def test_find(self):
        list2 = LinkedList2()

        self.assertEqual(list2.find(55), None)
        self.assertEqual(list2.find(None), None)
        list2.add_in_tail(Node(55))
        self.assertEqual(list2.find(55).value, 55)
        list2.add_in_tail(Node(12))
        list2.add_in_tail(Node(55))
        self.assertEqual(list2.find(55).value, 55)

    def test_find_all(self):
        list2 = LinkedList2()

        self.assertEqual(list2.find_all(None), [])
        self.assertEqual(list2.find_all(55), [])
        list2.add_in_tail(Node(55))
        list2.add_in_tail(Node(12))
        list2.add_in_tail(Node(55))
        result = [node.value for node in list2.find_all(55)]
        self.assertEqual(result, [55, 55])

    def test_delete(self):
        list1 = LinkedList2()
        list1.add_in_tail(Node(12))
        list1.add_in_tail(Node(43))
        list1.add_in_tail(Node(10))
        list1.add_in_tail(Node(14))
        list1.delete(43)
        self.assertEqual(list1.find(12).next.value, 10)
        self.assertEqual(list1.find(10).prev.value, 12)

    def test_add_in_head(self):
        list3 = LinkedList2()
        self.assertEqual(list_linkedlist(list3), [])

        list3.add_in_head(Node(55))
        self.assertEqual(list3.head.value, 55)
        self.assertEqual(list3.tail.value, 55)
        self.assertEqual(list3.len(), 1)
        self.assertEqual(list_linkedlist(list3), [55])

        list3.add_in_head(Node(12))
        list3.add_in_head(Node(55))
        self.assertEqual(list3.head.value, 55)
        self.assertEqual(list3.tail.value, 55)
        self.assertEqual(list3.len(), 3)
        self.assertEqual(list_linkedlist(list3), [55, 12, 55])

    def test_insert1(self):
        list2 = LinkedList2()
        list2.insert(None, Node(12))
        self.assertEqual(list_linkedlist(list2), [12])

    def test_insert2(self):
        list2 = LinkedList2()
        list2.add_in_tail(Node(55))
        list2.insert(None, Node(12))
        self.assertEqual(list_linkedlist(list2), [55, 12])
        
    def test_insert3(self):
        list2 = LinkedList2()
        list2.add_in_tail(Node(55))
        list2.insert(Node(55), Node(12))
        self.assertEqual(list_linkedlist(list2), [55, 12])

if __name__ == '__main__':
    unittest.main()