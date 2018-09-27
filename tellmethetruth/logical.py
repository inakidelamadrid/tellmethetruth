import operator


def logic_evaluation(node):
    if node is LogicalNode:
        return node.test()
    elif type(node.value) in (int, bool):
        # relying on bool for every object is a risk, since any object that is not
        # None evaluates to True
        return bool(node.value)
    else:
        return node.value.to_bool()


class Node():
    def __init__(self):
        self.left = None
        self.right = None


class ValueNode(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def test(self):
        self.bool_value = logic_evaluation(self)
        return self.bool_value


class LogicalNode(Node):
    OR = 'or'
    AND = 'and'
    NOT = 'not'

    def __init__(self, op):
        self.op_name = op

        # the operator module attribute needs an appended _
        self._op = getattr(operator, "{}_".format(op))

    def __str__(self):
        return self.op_name

    @classmethod
    def factory(klass, op):
        return {
            'or': ORNode,
            'and': ANDNode,
            'not': NOTNode
        }[op]()


class NOTNode(LogicalNode):
    def valid(self):
        # right must be None
        return self.left and not self.right

    def test(self):
        self.bool_value = not self.left.test()
        return self.bool_value


class BinomialLogicalNode(LogicalNode):
    def valid(self):
        # left and right must not be None
        return self.left and self.right

    def test(self):
        left_value = self.left.test()
        right_value = self.right.test()
        self.bool_value = self._op(left_value, right_value)
        return self.bool_value


class ORNode(BinomialLogicalNode):
    def __init__(self):
        super().__init__('or')


class ANDNode(BinomialLogicalNode):
    def __init__(self):
        super().__init__('and')


class LogicalTree(object):
    pass


def cast_node(obj):
    if issubclass(type(obj), LogicalNode):
        return obj
    elif issubclass(type(obj), LogicalTree):
        return obj.root
    return ValueNode(obj)
