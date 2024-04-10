from Linked_list import Node, LinkedList

def Linked_list_sum(list1: LinkedList, list2: LinkedList):

    if list1.len() != list2.len():
        return None

    list_sum = LinkedList()
    node1, node2 = list1.head, list2.head

    while node1 is not None:
        node_sum = Node(node1.value + node2.value)
        list_sum.add_in_tail(node_sum)
        node1, node2 = node1.next, node2.next
    return list_sum

