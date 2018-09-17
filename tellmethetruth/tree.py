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


def logic_evaluation(obj):
    # relying on bool for every object is a risk, since any object that is not
    # None evaluates to True
    if type(obj) in (int, bool):
        return bool(obj)
    else:
        return obj.to_bool()


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    IN_ORDER = '_inorder'
    POST_ORDER = '_postorder'
    PRE_ORDER = '_preorder'

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def height(self):
        return height(self.root)

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._add(value, node.right)
            else:
                node.right = Node(value)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):
        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            return self._find(value, node.left)
        elif value > node.value and node.right is not None:
            return self._find(value, node.right)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value)
            self._inorder(node.right)

    def _preorder(self, node):
        if node:
            print(node.value)
            self._preorder(node.left)
            self._preorder(node.right)

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.value)

    def traverse(self, order=IN_ORDER):
        getattr(self, order)(self.root)
