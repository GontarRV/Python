class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        index = 0
        for ch in value:
            index += (self.step + ord(ch)) * ord(ch)
        return index % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        for _i in range(self.size):
            if self.slots[index] is None:
                return index
            index += self.step
            index = index % self.size
        return None

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
            return index
        return None        

    def find(self, value):
        index = self.hash_fun(value)
        for _i in range(self.size):
            if self.slots[index] == value:
                return index
            index += self.step
            index = index % self.size
        return None
    
    