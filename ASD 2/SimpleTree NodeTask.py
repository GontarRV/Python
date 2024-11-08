# 1. Напишите метод, который перебирает 
# всё дерево и прописывает каждому узлу его уровень.

    def _set_level_nodes(self, node):
        if node is self.Root:
            node.Level = 0
        for child in node.Children:
            child.Level = child.Parent.Level + 1
            self._set_level_nodes(child)

    def SetLevelNodes(self):
        self._set_level_nodes(self.Root)

# 3.* (бонус +500) Добавьте метод проверки, 
# симметрично ли дерево относительно своего корня.

    def _is_symmetric(tree: list) -> bool:
        start = 0
        end = 2
        while start < len(tree):
            stratum = tree[start:end]
            if len(stratum) != (end - start) or stratum != list(reversed(stratum)):
                return False
            start = end
            end = 2 * end  + 2
        return True

    def symmetric(Tree: SimpleTree):
        return _is_symmetric(Tree.Root.Children)

    