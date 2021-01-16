class LiteralNode:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f'({self.value})'


class BinOpNode:
    def __init__(self, left, op: str, right):
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self):
        return f'({self.left} {self.op} {self.right})'


class UnOpNode(LiteralNode):
    def __init__(self, op: str, right):
        super().__init__(str(float(op + right.value)))
        self.op = op
        self.right = right
    def __repr__(self):
        return f'({self.op} {self.right})'


class NumberNode(LiteralNode):
    def __init__(self, num):
        super().__init__(num)
        self.num = num
    def __repr__(self):
        return f'({self.num})'