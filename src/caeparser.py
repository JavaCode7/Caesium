import caetoken, caenodes

class CaeParser:
    def __init__(self, tokens):
        self.ast: list = []
        self.tokens: list = tokens
        self.current: caetoken.CaeToken = None
        self.index: int = 0
        self.current = self.tokens[self.index]
        self.signals = {"num": True, "5-4": False}

    def advance(self, amount: int = 1):
        self.index += amount
        try:
            self.current = self.tokens[self.index]
        except IndexError:
            self.current = "cae-end-of-file"

    def parse(self):
        while self.current != "cae-end-of-file":
            self.ast.append(self.exprLevel4())
            self.advance()
        for i in range(len(self.ast) - 1, -1, -1):
            if self.ast[i] == None:
                del self.ast[i]

    #? Literals
    def exprLevel1(self):
        if not self.signals["num"]:
            self.advance(-1)
        if self.current.type in ("INTEGER", "FLOAT"):
            return caenodes.NumberNode(str(self.current.value))
        elif self.current.type in ("MINUS", "PLUS"):
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
        if self.current.type in ("INTEGER", "FLOAT"):
            self.advance(2)
            if self.current == "cae-end-of-file":
                self.advance(-2)
                return self.exprLevel1()
            else:
                self.signals["num"]: bool == False
                self.advance(-2)
                left = self.exprLevel1()
                self.advance()
                if self.current.type in ("MUL", "DIV"):
                    op = self.current.value
                    self.advance()
                    if self.current.type in ("INTEGER", "FLOAT"):
                        right = self.exprLevel4()
                        return caenodes.BinOpNode(left, op, right)
        else:
            return self.exprLevel1()

    #? Plus/Minus
    def exprLevel5(self):
        pass

    #? Base
    def exprLevel6(self):
        pass