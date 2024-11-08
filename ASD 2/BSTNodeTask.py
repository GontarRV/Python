#1.* Добавьте метод, проверяющий, идентично ли 
# текущее дерево дереву-параметру.

def are_identic_trees(self, tree: BST):
        return self._are_identic(self.Root, tree.Root)
	
def _are_identic(self, node1: BSTNode, node2: BSTNode):
    if (node1 is None) and (node2 is None):
        return True
    
    if (node1 is not None) and (node2 is not None):
        if node1.NodeKey != node2.NodeKey:
            return False
        left = self._are_identic(node1.LeftChild, node2.LeftChild)
        right = self._are_identic(node1.RightChild, node2.RightChild)
        return all([left, right])
    return False

# 2.* (бонус +500) Добавьте метод, который нахождит все 
# пути от корня к листьям, длина которых равна заданной величине.




# 3.* (бонус +500) Добавьте метод, который находит все пути от корня 
# к листьям, чтобы сумма значений узлов на этом пути была максимальной.