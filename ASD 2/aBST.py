class aBST:

    def __init__(self, depth: int):
        tree_size = 2**(depth + 1) - 1
        self.Tree = [None] * tree_size  # массив ключей

    def _find_index(self, key: int, index: int) -> int:
        if index >= len(self.Tree):
            return None
        if not self.Tree[index]:
            return -index
        if self.Tree[index] == key:
            return index
        if self.Tree[index] > key:
            return self._find_index(key, 2 * index + 1)
        if self.Tree[index] < key:
            return self._find_index(key, 2 * index + 2)

    def _add_key(self, key: int, index: int) -> int:
        if index >= len(self.Tree):
            return -1
        if self.Tree[index] is None:
            self.Tree[index] = key
            return index
        if self.Tree[index] > key:
            return self._add_key(key, 2 * index + 1)
        if self.Tree[index] < key:
            return self._add_key(key, 2 * index + 2)
        if self.Tree[index] == key:
            return index

    def FindKeyIndex(self, key: int) -> int:
        if self.Tree[0] is None:
            return None
        return self._find_index(key, 0)

    def AddKey(self, key: int) -> int:
        return self._add_key(key, 0)