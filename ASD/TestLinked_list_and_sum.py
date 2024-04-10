import unittest

from Linked_list import LinkedList, Node
from linked_list_sum import Linked_list_sum


def list_linkedlist(l):
    result = []
    node = l.head
    while node is not None:
        result.append(node.value)
        node = node.next
    return result


class TestLinkedList(unittest.TestCase):
    def test_add_in_tail(self):
        list1 = LinkedList()
        list1.add_in_tail(Node(7))

    def test_len(self):
        list2 = LinkedList()
        self.assertEqual(list2.len(), 0)

        list2.add_in_tail(Node(8))
        self.assertEqual(list2.len(), 1)

        list2.add_in_tail(Node(10))
        list2.add_in_tail(Node(7))
        self.assertEqual(list2.len(), 3)

    def test_clean_list(self):
        list2 = LinkedList()
        list2.add_in_tail(Node(3))
        list2.add_in_tail(Node(8))

        list2.clean()
        self.assertIsNone(list2.head)

    def test_find_node_in_empty_list(self):
        list2 = LinkedList()
        self.assertIsNone(list2.find(9))

    def test_find_node(self):
        list2 = LinkedList()
        list2.add_in_tail(Node(12))
        list2.add_in_tail(Node(55))
        list2.add_in_tail(Node(128))
        self.assertEqual(list2.find(55).value, 55)

    def test_find_all_nodes(self):
        list2 = LinkedList()
        self.assertEqual(list2.find_all(55), [])

        list2.add_in_tail(Node(12))
        list2.add_in_tail(Node(55))
        list2.add_in_tail(Node(128))
        list2.add_in_tail(Node(55))
        list2.add_in_tail(Node(55))
        list2.add_in_tail(Node(55))

        result = [node.value for node in list2.find_all(55)]
        self.assertEqual(result, [55, 55, 55, 55])

    def test_delete_all_nodes(self):
        list2 = LinkedList()
        list2.delete(55, all=True)
        self.assertEqual(list_linkedlist(list2), [])

        list2.add_in_tail(Node(12))
        list2.add_in_tail(Node(55))
        list2.add_in_tail(Node(128))
        list2.add_in_tail(Node(12))
        list2.add_in_tail(Node(55))
        list2.add_in_tail(Node(128))
        list2.delete(55, all=True)
        self.assertEqual(list_linkedlist(list2), [12, 128, 12, 128])

    def test_insert1(self):
        list2 = LinkedList()
        list2.insert(None, Node(12))
        self.assertEqual(list_linkedlist(list2), [12])

    def test_insert2(self):
        list2 = LinkedList()
        list2.add_in_tail(Node(55))
        list2.insert(None, Node(12))
        self.assertEqual(list_linkedlist(list2), [12, 55])
        
    def test_insert3(self):
        list2 = LinkedList()
        list2.add_in_tail(Node(55))    
        list2.insert(Node(55), Node(12))
        self.assertEqual(list_linkedlist(list2), [55, 12])


class TestSumTwoLists(unittest.TestCase):
    def test_sum_yes(self):
        list1 = LinkedList()
        list2 = LinkedList()

        list1.add_in_tail(Node(12))
        list1.add_in_tail(Node(55))
        list1.add_in_tail(Node(128))

        list2.add_in_tail(Node(1))
        list2.add_in_tail(Node(2))
        list2.add_in_tail(Node(3))

        self.assertEqual(list_linkedlist(Linked_list_sum(list1, list2)), [13, 57, 131])

    def test_sum_no(self):
        list1 = LinkedList()
        list2 = LinkedList()

        list1.add_in_tail(Node(12))
        list1.add_in_tail(Node(55))
        list1.add_in_tail(Node(128))

        list2.add_in_tail(Node(1))
        list2.add_in_tail(Node(2))

        self.assertEqual(Linked_list_sum(list1, list2), None)


if __name__ == '__main__':
    unittest.main()