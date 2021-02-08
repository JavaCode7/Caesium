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


class NumberNode(LiteralNode):
    def __init__(self, num):
        super().__init__(num)
        self.num = num
    def __repr__(self):
        return f'({self.num})'


class StringNode(LiteralNode):
    def __init__(self, string):
        super().__init__(string)
        self.string = string
    def __repr__(self):
        return f'({self.string})'


class CharNode(StringNode):
    def __init__(self, string):
        super().__init__(string)
        self.string = string
    def __repr__(self):
        return f'({self.string})'