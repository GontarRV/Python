class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0

    def hash1(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result = result * 17 + code
        return result % self.filter_len

    def hash2(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result = result * 223 + code
        return result % self.filter_len

    def add(self, str1):
        self.filter = self.filter | self.hash1(str1)
        self.filter = self.filter | self.hash2(str1)

    def is_value(self, str1):
        hash1 = self.filter & self.hash1(str1)
        hash2 = self.filter & self.hash2(str1)
        return hash1 > 0 and hash2 > 0