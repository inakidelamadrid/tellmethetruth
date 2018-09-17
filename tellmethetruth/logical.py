import operator


def logic_evaluation(obj):
    # relying on bool for every object is a risk, since any object that is not
    # None evaluates to True
    if type(obj) in (int, bool):
        return bool(obj)
    else:
        return obj.to_bool()


class LogicalNode(object):
    def __init__(self, op):
        self.__op = getattr(operator, op)


class NOTNode(LogicalNode):
    def __init__(self):
        super().__init__('not_')

    def valid(self):
        # right must be None
        return self.left and not self.right

    def test(self):
        return not logic_evaluation(self.left.value)


class BinomialLogicalNode(LogicalNode):
    def valid(self):
        # left and right must not be None
        return self.left and self.right

    def test(self):
        left_eval = logic_evaluation(self.left.value)
        right_eval = logic_evaluation(self.right.value)
        return self.__op(left_eval, right_eval)


class ORNode(BinomialLogicalNode):
    def __init__(self):
        super().__init__('or_')


class ANDNode(BinomialLogicalNode):
    def __init__(self):
        super().__init__('and_')


class LogicalTree(object):
    pass
