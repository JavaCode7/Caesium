import caebuiltins

class CaeInterpreter:

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)
    
    def visit_BinOpNode(self, node):
        if node.op == "*":
            return caebuiltins.Float(
                caebuiltins.Float(node.left.num).mul(caebuiltins.Float(node.right.num))
            )
        elif node.op == "/":
            return caebuiltins.Float(
                caebuiltins.Float(node.left.num).div(caebuiltins.Float(node.right.num))
            )
    
    def visit_NumberNode(self, node):
        try:
            return caebuiltins.Int(node.num)
        except ValueError:
            return caebuiltins.Float(node.num)