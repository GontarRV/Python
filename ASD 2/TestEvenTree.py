import unittest
from EvenTree import SimpleTree, SimpleTreeNode

class TestSimpleTree(unittest.TestCase):

    def create_test_tree():

        root_node = SimpleTreeNode(9, None)
        tree = SimpleTree(root_node)

        node_4 = SimpleTreeNode(4, None)
        tree.AddChild(tree.Root, node_4)

        node_3 = SimpleTreeNode(3, None)
        tree.AddChild(node_4, node_3)

        node_6 = SimpleTreeNode(6, None)
        tree.AddChild(node_4, node_6)

        node_5 = SimpleTreeNode(5, None)
        tree.AddChild(node_6, node_5)

        node_7 = SimpleTreeNode(7, None)
        tree.AddChild(node_6, node_7)

        node_17 = SimpleTreeNode(17, None)
        tree.AddChild(tree.Root, node_17)

        node_22 = SimpleTreeNode(22, None)
        tree.AddChild(node_17, node_22)

        node_20 = SimpleTreeNode(20, None)
        tree.AddChild(node_22, node_20)

        return tree, [root_node, node_4, node_3, node_6, node_5,
                  node_7, node_17, node_22, node_20]
    
    def test_even_tree(self) -> None:
        node_1 = SimpleTreeNode(1, None)
        tree = SimpleTree(node_1)
        node_2 = SimpleTreeNode(2, None)
        node_5 = SimpleTreeNode(5, None)
        node_7 = SimpleTreeNode(7, None)
        node_3 = SimpleTreeNode(3, None)
        node_6 = SimpleTreeNode(6, None)
        node_4 = SimpleTreeNode(6, None)
        node_8 = SimpleTreeNode(6, None)
        node_9 = SimpleTreeNode(6, None)
        node_10 = SimpleTreeNode(6, None)
        tree.AddChild(tree.Root, node_2)
        tree.AddChild(tree.Root, node_3)
        tree.AddChild(tree.Root, node_6)
        tree.AddChild(node_2, node_5)
        tree.AddChild(node_2, node_7)
        tree.AddChild(node_3, node_4)
        tree.AddChild(node_6, node_8)
        tree.AddChild(node_8, node_9)
        tree.AddChild(node_8, node_10)

        self.assertListEqual(tree.EvenTrees(), [node_1, node_3, node_1, node_6])
        
if __name__ == "__main__":
    unittest.main()