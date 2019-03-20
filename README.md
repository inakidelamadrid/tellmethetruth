# tellmethetruth
Evaluation tree for boolean or composite objects

# Binary Trees

## Build the simplest tree
tellmethetruth is bases on building and nesting `BinaryTree` objects from its `tree` module

```python
  from tellmethetruth.tree import BinaryTree
  from tellmethetruth.logical import LogicalNode

  
  root = BinaryTree(left=True, right=False, op=LogicalNode.OR)
  # same as
  # BinaryTree(True, True, LogicalNode.OR)
  root.evaluate()   # > True

  root2 = BinaryTree(left=True, right=False, op=LogicalNode.AND)
  root2.evaluate()  # > False

  # it also can evaluate integers

  root3 = BinaryTree(left=1, right=0, op=LogicalNode.AND)
  root3.evaluate()  # > False

  root4 = BinaryTree(left=1, right=1, op=LogicalNode.AND)
  root4.evaluate()  # > True
```

#
