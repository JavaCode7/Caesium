class CaeInterpreter:

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)
    
    def visit_BinOpNode(self, node):
        return eval(f"{node.left}{node.op}{self.visit(node.right)}")
    
    def visit_NumberNode(self, node):
        return node.num