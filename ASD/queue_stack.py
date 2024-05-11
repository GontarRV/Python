class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop(self.size() - 1)  
        return None 

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() > 0:
            return self.stack[self.size() - 1] 
        return None

class Queue:
    def __init__(self):
        self.queue1 = Stack()
        self.queue2 = Stack()

    def enqueue(self, item):
        self.queue1.append(item)

    def dequeue(self):
        if self.size() > 0:
            if self.queue1.size() > 0:
                self.queue2.push(self.queue1.pop())
            return self.queue2.pop()
        return None

    def size(self):
        return len(self.queue1) + len(self.queue2)