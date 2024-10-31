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
  
    def DeleteNode(self, NodeToDelete):
        NodeToDelete.Parent.Children.remove(NodeToDelete)

    def GetAllNodes(self) -> list:
        if self.Root is None:
            return []
        return self._get_all_nodes(self.Root)

    def FindNodesByValue(self, val) -> list:
        return self._find_nodes_by_value(self.Root, val)
   
    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)
   
    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        return len([node for node in self.GetAllNodes() if not node.Children])

    def SetLevelNodes(self):
        self.__set_level_nodes(self.Root)

    def AssignLevels(self):
        if self.Root is None:
            return
        self.Root.Level = 1
        for node in self.GetAllNodes():
            if node.Parent is not None:
                node.Level = node.Parent.Level + 1


    def _get_all_nodes(self, node):
        nodes = []
        nodes.append(node)
        for child in node.Children:
            nodes += self._get_all_nodes(child)
        return nodes

    def _find_nodes_by_value(self, node, value):
        nodes = []
        if node.NodeValue == value:
            nodes.append(node)
        for i in node.Children:
            nodes.extend(self._find_nodes_by_value(i, value))
        return nodes

    def _set_level_nodes(self, node):
        if node is self.Root:
            node.Level = 0
        for child in node.Children:
            child.Level = child.Parent.Level + 1
            self._set_level_nodes(child)