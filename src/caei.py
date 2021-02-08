import caebuiltins

class CaeInterpreter:

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)
    
    def visit_BinOpNode(self, node):
        left: caebuiltins.Value = self.visit(node.left)
        right: caebuiltins.Value = self.visit(node.right)
        if node.op == "*":
            if isinstance(left.mul(right), int):
                return caebuiltins.Int(left.mul(right))
            else:
                try:
                    return caebuiltins.Float(left.mul(right))
                except ValueError:
                    return caebuiltins.String(left.mul(right))
        elif node.op == "/":
            return caebuiltins.Float(left.div(right))
        elif node.op == "+":
            if isinstance(left.mul(right), int):
                return caebuiltins.Int(left.plus(right))
            else:
                try:
                    return caebuiltins.Float(left.plus(right))
                except ValueError:
                    return caebuiltins.String(left.plus(right))
        elif node.op == "-":
            if isinstance(left.mul(right), int):
                return caebuiltins.Int(left.minus(right))
            else:
                return caebuiltins.Float(left.minus(right))

    def visit_NumberNode(self, node):
        try:
            return caebuiltins.Int(node.num)
        except ValueError:
            return caebuiltins.Float(node.num)

    def visit_StringNode(self, node):
        return caebuiltins.String(node.string)

    def visit_CharNode(self, node):
        return caebuiltins.Char(node.string)