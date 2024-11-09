class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        

class BSTFind:
    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:
    def __init__(self, node):
        self.Root = node
        
    def FindNodeByKey(self, key):
        if self.Root is None:
            return BSTFind()
        
        return self._FindNodeByKeyRecursive(key, self.Root)

    def AddKeyValue(self, key, val):
        if self.Root is None:
            self.Root = BSTNode(key, val, parent=None)
            return True
        return self._add_key_value(self.Root, key, val)
  
    def FinMinMax(self, FromNode, FindMax: bool):
        if (FindMax and FromNode.RightChild is None) or (not FindMax and FromNode.LeftChild is None):
            return FromNode
        elif FindMax:
            return self.FinMinMax(FromNode.RightChild, FindMax)
        else:
            return self.FinMinMax(FromNode.LeftChild, FindMax)
	
    def DeleteNodeByKey(self, key):

        findResult = self.FindNodeByKey(key)
        
        if not findResult.NodeHasKey:
            return False
        node = findResult.Node

        if node.LeftChild is None or node.RightChild is None:
            self._DeleteNodeWithMaxOneChild(node)
            return True
        
        parent = findResult.Node.Parent
        successor = self.FinMinMax(node.RightChild, False)
        self._DeleteNodeWithMaxOneChild(successor)
        successor.LeftChild = node.LeftChild
        successor.RightChild = node.RightChild
        node.LeftChild.Parent = successor

        if node.RightChild is not None:
            node.RightChild.Parent = successor

        successor.Parent = parent

        if parent is None:
            self.Root = successor
        elif successor.NodeKey < parent.NodeKey:
            parent.LeftChild = successor
        else:
            parent.RightChild = successor
        
        return True

    def Count(self):
        self._counter = 0

        if self.Root is not None:
            self._CountNodes(self.Root)

        return self._counter

    def _FindNodeByKeyRecursive(self, key, currentNode):
        if key < currentNode.NodeKey and currentNode.LeftChild is not None:
            return self._FindNodeByKeyRecursive(key, currentNode.LeftChild)
        elif key > currentNode.NodeKey and currentNode.RightChild is not None:
            return self._FindNodeByKeyRecursive(key, currentNode.RightChild)
        
        result = BSTFind()
        result.Node = currentNode
        
        if key == currentNode.NodeKey:
             result.NodeHasKey = True
        elif key < currentNode.NodeKey:
            result.ToLeft = True
        
        return result

    def _add_key_value(self, Node, key, value):
        if Node.NodeKey == key:
            return False
        if (Node.NodeKey < key) and (Node.RightChild is None):
            Node.RightChild = BSTNode(key, value, Node)
            return True
        if (Node.NodeKey > key) and (Node.LeftChild is None):
            Node.LeftChild = BSTNode(key, value, Node)
            return True
        if Node.NodeKey < key:
            return self._add_key_value(Node.RightChild, key, value) 
        return self._add_key_value(Node.LeftChild, key, value)

    def _DeleteNodeWithMaxOneChild(self, node):
        parent = node.Parent
        successor = None

        if node.RightChild is not None:
            successor = node.RightChild
        elif node.LeftChild is not None:
            successor = node.LeftChild

        if parent is None:
            self.Root = successor
        elif node.NodeKey < parent.NodeKey:
            parent.LeftChild = successor
        else:
            parent.RightChild = successor

        if successor is not None:
            successor.Parent = parent

    def _CountNodes(self, currentNode):
        self._counter += 1
        
        if currentNode.LeftChild is not None:
            self._CountNodes(currentNode.LeftChild)
        if currentNode.RightChild is not None:
            self._CountNodes(currentNode.RightChild)

    def WideAllNodes(self) -> tuple:
        if not self.Root:
            return ()
        all_nodes = []
        nodes_in_level = [self.Root]
        while nodes_in_level:
            node = nodes_in_level.pop(0)
            all_nodes.append(node)
            if node.LeftChild:
                nodes_in_level.append(node.LeftChild)
            if node.RightChild:
                nodes_in_level.append(node.RightChild)
        return tuple(all_nodes)
    
    def DeepAllNodes(self, value):
        if not self.Root:
            return 

        all_nodes = []
        if value == 0:
            self._in_order_deepallnodes(self.Root, all_nodes)
        if value == 1:
            self._post_order_deepallnodes(self.Root, all_nodes)
        if value == 2:
            self._pre_order_deepallnodes(self.Root, all_nodes)
        return tuple(all_nodes)

    def _in_order_deepallnodes(self, node, all_nodes):
        if node:
            self._in_order_deepallnodes(node.LeftChild, all_nodes)
            all_nodes.append(node)
            self._in_order_deepallnodes(node.RightChild, all_nodes)

    def _post_order_deepallnodes(self, node, all_nodes):
        if node:
            self._post_order_deepallnodes(node.LeftChild, all_nodes)
            self._post_order_deepallnodes(node.RightChild, all_nodes)
            all_nodes.append(node)
        
    def _pre_order_deepallnodes(self, node, all_nodes):
        if node:
            all_nodes.append(node)
            self._post_order_deepallnodes(node.LeftChild, all_nodes)
            self._post_order_deepallnodes(node.RightChild, all_nodes)
