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

## Building a tree with custom classes
tellmethe truth can evaluate custom class instances as long as they declare a `to_bool` method. As its name says, it must return a boolean representation of the object.

```python
from tellmethetruth.tree import BinaryTree
from tellmethetruth.logical import LogicalNode


# we can test a tree of manga lovers
class Person:
  def __init__(self, name, hobbies=[]):
    self.name = name
    self.hobbies = hobbies

  def to_bool(self):
    return 'manga' in self.hobbies


inaki = Person('Inaki', ['manga', 'board games'])
vader = Person('Darth', ['power', 'dark force'])

mangalovers_tree = BinaryTree(inaki, vader, LogicalNode.AND)
mangalovers_tree.evaluate()  # > False
```

## Using nested trees
We can nest trees within our root and thus we have leafs. 

```python
from tellmethetruth.tree import BinaryTree
from tellmethetruth.logical import LogicalNode

# we can test a tree of manga lovers
class Person:
  def __init__(self, name, hobbies=[]):
    self.name = name
    self.hobbies = hobbies

  def to_bool(self):
    return 'manga' in self.hobbies


inaki = Person('Inaki', ['manga', 'board games'])
vader = Person('Darth', ['lightsaber', 'dark force'])
yoda = Person('Darth', ['lightsaber', 'manga'])

masters = BinaryTree(vader, yoda, LogicalNode.OR)
mangalovers_tree = BinaryTree(inaki, masters, LogicalNode.AND)
mangalovers_tree.evaluate()  # > True
```

## Simplify tree building
Use tellmethetruth utils module's functions to easily create AND and OR trees.

```python
from tellmethetruth.tree import BinaryTree
from tellmethetruth.utils import logical_and_tree, logical_or_tree

# we can test a tree of manga lovers
class Person:
  def __init__(self, name, hobbies=[]):
    self.name = name
    self.hobbies = hobbies

  def to_bool(self):
    return 'manga' in self.hobbies


inaki = Person('Inaki', ['manga', 'board games'])
vader = Person('Darth', ['lightsaber', 'dark force'])
yoda = Person('Darth', ['lightsaber', 'manga'])

masters = logical_or_tree(vader, yoda)
mangalovers_tree = logical_and_tree(inaki, masters)
mangalovers_tree.evaluate()  # > True
```
