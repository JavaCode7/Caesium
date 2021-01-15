class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self):
        return f'({self.left} {self.op} {self.right})'


class UnOpNode:
    def __init__(self, op, right):
        self.op = op
        self.right = right
    def __repr__(self):
        return f'({self.op} {self.right})'

        
class NumberNode:
    def __init__(self, num):
        self.num = num
    def __repr__(self):
        return f'({self.num})'