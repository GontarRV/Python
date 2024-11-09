from SimpleTreeNode import SimpleTreeNode, SimpleTree

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
    stratum = []
    child_nodes = None
    for n in tree:
        stratum.extend(n.Children)
        if child_nodes is None:
            child_nodes = len(n.Children)
        if child_nodes != len(n.Children):
            return False

    if stratum:
        return _is_symmetric(stratum)
    return True

def symmetric(Tree: SimpleTree):
    return _is_symmetric(Tree.Root.Children)