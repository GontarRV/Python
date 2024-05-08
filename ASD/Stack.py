class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    # O(N)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop(0)  
        return None 

    # O(N)
    def push(self, value):
        self.stack.insert(0, value) 
        return self.stack[0]

    def peek(self):
        if self.size() > 0:
            return self.stack[0] 
        return None 

def balance(staples: str) -> bool:
    stack = Stack()
    for bracket in staples:
        if bracket == '(':
            stack.push(bracket)
            continue
        if bracket == ')' and stack.peek() == '(':
            stack.pop()
            continue
        return False
    return stack.size() == 0