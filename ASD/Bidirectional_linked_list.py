class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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
        
        node = self.head

        while node is not None:
            if node.value == val:
                if node == self.head:
                    self.head = node.next
                    if self.head != None:
                        self.head.prev = None

                if node.next == None:
                    self.tail = node.prev
                    if self.tail != None:
                        self.tail.next = None
                    node = None

                if node != None and node.prev != None:
                    node.prev.next = node.next
                    node.next.prev = node.prev

                if node != None:
                    node = node.next

                if not all:
                    return
            else:
                node = node.next

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
        if afterNode is None and self.head is None:
            self.head = newNode
            return

        if afterNode is None and self.head is not None:
            self.add_in_tail(newNode)
            return
        
        node = self.head
        while node is not None:
            if node.value != afterNode.value:
                node = node.next
                continue
            newNode.next = node.next
            newNode.prev = node

            if node.next is None:
                self.tail = newNode
            
            if node.next is not None:
                self.tail.prev = newNode
            node.next = newNode
            break

    def add_in_head(self, newNode):
        if newNode is None:
            return

        if self.tail is None:
            self.tail = newNode
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head

        self.head = newNode
