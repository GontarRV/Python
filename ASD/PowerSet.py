class PowerSet():

    def __init__(self):
        self.list = []

    def size(self):
        return len(self.list)

    def put(self, value):
        if self.get(value) is False:
            self.list.append(value)

    def get(self, value):
        for i in self.list:
            if i == value:
                return True
        return False

    def remove(self, value):
        if self.get(value) is False:
            return False
        self.list.remove(value)
        return True

    def intersection(self, set2):
        result = PowerSet()
        for i in self.list:
            if set2.get(i) is True:
                result.put(i)
        return result

    def union(self, set2):
        result = PowerSet()
        if set2.size == 0:
            return self.list
        for i in self.list:
            result.put(i)
        for i in set2.list:
            result.put(i)
        return result

    def difference(self, set2):
        result = PowerSet()
        for i in self.list:
            result.put(i)
        for i in set2.list:
            if self.get(i) is True:
                result.remove(i)
        return result

    def issubset(self, set2):
        for i in set2.list:
            if not self.get(i):
                return False
        return True