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

    def __nodes_to_remove_edge(self, node: SimpleTreeNode, nodes_remove_edge: list):
        count = 1
        for child in node.Children:
            count += self.__nodes_to_remove_edge(child, nodes_remove_edge)
        if count % 2 == 0 and node.Parent:
            nodes_remove_edge.append(node.Parent)
            nodes_remove_edge.append(node)
            count = 0
        return count

    def EvenTrees(self):
        if not self.Root:
            return []
        roots_even_trees = []
        self.__nodes_to_remove_edge(self.Root, roots_even_trees)
        return roots_even_trees