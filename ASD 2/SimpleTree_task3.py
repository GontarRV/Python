class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов
	
class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None
	
    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode



    def _is_symmetric(self,
                      left_children: list[SimpleTreeNode],
                      right_children: list[SimpleTreeNode]):
        for left_child, right_child in zip(left_children, reversed(right_children)):
            if left_child.NodeValue != right_child.NodeValue:
                return False
            if len(left_child.Children) != len(right_child.Children):
                return False
            if not self._is_symmetric(left_child.Children, right_child.Children):
                return False
        return True

    def symmetric(self):
        if not self.Root:
            return True

        if len(self.Root.Children) % 2 != 0:
            return False

        return self._is_symmetric(self.Root.Children[:(len(self.Root.Children) // 2)],
                                  self.Root.Children[(len(self.Root.Children) // 2):])