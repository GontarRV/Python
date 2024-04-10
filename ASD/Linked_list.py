class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result_l = []
        node = self.head
        while node is not None:
            if node.value == val:
                result_l.append(node)
            node = node.next
        return result_l

    def delete(self, val, all=False):
        if self.head is None:
            return
        
        node_del, node_p = self.head, self.head

        while node_del is not None:
            if node_del.value == val and node_del == self.head:
                self.head = self.head.next
                if self.head is None:
                    self.tail = None
                if not all:
                    break
                node_del = self.head
                continue
            if node_del.value == val and node_del == self.tail:
                node_p.next = None
                self.tail = node_p

            if node_del.value == val:
                node_p.next = node_del.next
                node_del.next = None
                if not all:
                    break
                node_del = node_p.next
                continue
            node_p = node_del
            node_del = node_del.next

    def clean(self):
        self.__init__()

    def len(self):
        len_v = 0
        node = self.head
        while node is not None:
            len_v += 1
            node = node.next
        return len_v

    def insert(self, afterNode, newNode):
        if self.head is None:
            self.tail = newNode
            self.head = newNode
            return
        
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            return
        
        node, node_p = self.head, self.head
        while node is not None:
            node_p = node
            node = node.next

            if node_p.value == afterNode.value and node_p == self.tail:
                newNode.next = node
                node_p.next = newNode
                self.tail = newNode
            
            if node_p.value == afterNode.value:
                newNode.next = node
                node_p.next = newNode

