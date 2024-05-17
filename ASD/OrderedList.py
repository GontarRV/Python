class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0

    def add(self, value):
        new_node = Node(value)
        node = self.head

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return new_node.value

        while node is not None:
            comparison = self.compare(new_node.value, node.value)
            if self.__ascending and comparison in (-1, 0) or (not self.__ascending and comparison in (1, 0)):
                new_node.prev = node.prev
                new_node.next = node

                if node.prev is None:
                    self.head = new_node
                if node.prev is not None:
                    node.prev.next = new_node

                node.prev = new_node
                return new_node.value
            node = node.next

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        return new_node.value

    def find(self, val):
        if self.head is None:
            return None
        
        if self.__ascending and (val < self.head.value or val > self.tail.value):
            return None

        if not self.__ascending and (val > self.head.value or val < self.tail.value):
            return None

        node = self.head
        while type(node) is Node:
            if self.__ascending and node.value > val:
                return None
            if not self.__ascending and node.value < val:
                return None

            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
        node = self.find(val)
        if node is None:
            return None

        if self.head is self.tail:
            self.clean(self.__ascending)
            return node.value

        if node is self.head:
            node.next.prev = None
            self.head = node.next
        elif node is self.tail:
            node.prev.next = None
            self.tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        return node.value

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        comp_v1 = v1.strip()
        comp_v2 = v2.strip()
        if comp_v1 < comp_v2:
            return -1
        if comp_v1 > comp_v2:
            return 1
        return 0