class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        slot = 0
        for ch in key:
            slot += self.size + ord(ch)
            slot *= ord(ch)
        return slot % self.size

    def is_key(self, key):
        if key in self.slots:
            return True
        return False

    def put(self, key, value):
        index1 = self.hash_fun(key)
        index = index1
        n = 0
        while self.slots[index] is not None:
            index = (index + 1) % self.size
            if n >= self.size:
                index = index1
                break
            n += 1
        self.slots[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash_fun(key)
        if not self.is_key(key):
            return None
        while self.slots[index] != key:
            index = (index + 1) % self.size
        return self.values[index]