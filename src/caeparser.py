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
            self.ast.append(self.exprLevel2())
            self.advance()
        if self.ast[len(self.ast) - 1] == None:
            del self.ast[1]
    #? Literals
    def exprLevel1(self):
        if self.current.type == "INTEGER" or self.current.type == "FLOAT":
            num: float = float(self.current.value)
            return caenodes.NumberNode(num)
        elif self.current.type == "MINUS" or self.current.type == "PLUS":
            op: str = self.current.value
            self.advance()
            num: float = float(op + str(self.current.value))
            return caenodes.NumberNode(num)
    #? Parentheses
    def exprLevel2(self):
        if self.current.type == "LPAREN":
            self.advance()
            while self.current.type != "RPAREN":
                return self.exprLevel2()
            self.advance()
        else:
            return self.exprLevel1()

    def exprLevel3(self):
        pass

    def exprLevel4(self):
        pass

    def exprLevel5(self):
        pass

    def exprLevel6(self):
        pass