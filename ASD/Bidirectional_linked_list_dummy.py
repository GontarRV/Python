class Node:
    def __init__(self, v = None):
        self.value = v
        self.prev = None
        self.next = None

class Dummy_node(Node):
    def __init__(self):
        super(Dummy_node, self).__init__()
        

class LinkedList2:
    def __init__(self):
        self.head = Dummy_node()
        self.tail = Dummy_node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, item):
        item.prev = self.tail.prev
        item.next = self.tail
        self.tail.prev.next = item
        self.tail.prev = item

    def find(self, val):
        node = self.head.next
        while type(node) is not Dummy_node:
            if node.value == val:
                return node
            node = node.next

    def find_all(self, val):
        result_l = []
        node = self.head.next
        while type(node) is not Dummy_node:
            if node.value == val:
                result_l.append(node)
            node = node.next
        return result_l

    def delete(self, val, all=False):
        
        node = self.head.next
        while type(node) is not Dummy_node:
            if node.value == val:
                node.prev.next = node.next 
                node.next.prev = node.prev
                if not all:
                    break
            node = node.next

    def clean(self):
        self.__init__()

    def len(self):
        len_v = 0
        node = self.head.next
        while type(node) is not Dummy_node:
            len_v += 1
            node = node.next
        return len_v

    def insert(self, afterNode, newNode):
        if afterNode is None and self.len() == 0:
            self.add_in_head(newNode)

        if afterNode is None and self.len() > 0:
            self.add_in_tail(newNode)
        else:
            newNode.prev = afterNode
            newNode.next = afterNode.next
            afterNode.next.prev = newNode
            afterNode.next = newNode
    
    def add_in_head(self, newNode):
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next.prev = newNode
        self.head.next = newNode
