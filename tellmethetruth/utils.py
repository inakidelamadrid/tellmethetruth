from .tree import BinaryTree
from .logical import LogicalNode


def build_tree(left, right, op):
    return BinaryTree(left, right, op)


def logical_or_tree(left, right):
    return build_tree(left, right, LogicalNode.OR)


def logical_and_tree(left, right):
    return build_tree(left, right, LogicalNode.AND)
