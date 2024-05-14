class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.size() > 0:
            return self.deque.pop(0)
        return None

    def removeTail(self):
        if self.size() > 0:
            return self.deque.pop(self.size() - 1)
        return None

    def size(self):
        return len(self.deque)

def palindromeCheck(inputString: list):
    deque1 = Deque()
    for item in inputString:
        deque1.addFront(item)
    while deque1.size() > 1:
        if deque1.removeFront() != deque1.removeTail():
            return False
    return True