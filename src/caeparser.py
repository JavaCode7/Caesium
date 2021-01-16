import caetoken, caenodes

class CaeParser:
    def __init__(self, tokens):
        self.ast: list = []
        self.tokens: list = tokens
        self.current: caetoken.CaeToken = None
        self.index: int = 0
        self.current = self.tokens[self.index]

    def advance(self, amount: int = 1):
        self.index += amount
        try:
            self.current = self.tokens[self.index]
        except IndexError:
            self.current = "cae-end-of-file"

    def parse(self):
        while self.current != "cae-end-of-file":
            self.ast.append(self.exprLevel1())
            self.advance()
        for i in range(len(self.ast) - 1, 0, -1):
            if self.ast[i] == None:
                del self.ast[i]

    #? Literals
    def exprLevel1(self):
        if self.current.type in ("INTEGER", "FLOAT"):
            return caenodes.NumberNode(str(self.current.value))
        if self.current.type in ("MINUS", "PLUS"):
            op: str = self.current.value
            self.advance()
            if self.current.type in ("INTEGER", "FLOAT"):
                return caenodes.NumberNode(op + str(self.current.value))

    #? Parentheses
    def exprLevel2(self):
        pass

    #? Exp
    def exprLevel3(self):
        pass

    #? Times/Div
    def exprLevel4(self):
        pass

    #? Plus/Minus
    def exprLevel5(self):
        pass

    #? Base
    def exprLevel6(self):
        pass