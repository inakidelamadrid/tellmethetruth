from .logical import LogicalTree, LogicalNode, cast_node


class BinaryTree(LogicalTree):
    def __init__(self, left, right, op):
        node = LogicalNode.factory(op)
        node.left = cast_node(left)
        node.right = cast_node(right)
        self.root = node

    def getRoot(self):
        return self.root

    def height(self):
        return height(self.root)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            node.test()

    def evaluate(self):
        self._postorder(self.root)
        return self.root.bool_value


def height(node):
    """ Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
    """
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

    # Use the larger one
    if lheight > rheight:
        return lheight + 1
    else:
        return rheight + 1
