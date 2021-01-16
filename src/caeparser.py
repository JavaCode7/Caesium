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
            self.ast.append(self.exprLevel3())
            self.advance()
        for i in range(len(self.ast) - 1, 0, -1):
            if self.ast[i] == None:
                del self.ast[i]

    #? Literals
    def exprLevel1(self):
        if self.current.type == "INTEGER" or self.current.type == "FLOAT":
            num = self.current
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
                return self.exprLevel3()
            self.advance()
        else:
            return self.exprLevel1()

    #? Exp
    def exprLevel3(self):
        if self.current.type == "INTEGER" or self.current.type == "FLOAT":
            left = self.current
            self.advance()
            print("step1", self.current)
            if self.current == "cae-end-of-file":
                self.advance(-1)
                return self.exprLevel2()

            if self.current.type == "POW":
                self.advance()
                print("step2", self.current)

                if self.current.type == "INTEGER" or self.current.type == "FLOAT":
                    right = self.current
                    return caenodes.BinOpNode(left, "**", right)

            else:
                self.advance(-1)
                print("else2", self.current)
                return self.exprLevel2()

        else:
            print("else1", self.current)
            return self.exprLevel2()

    def exprLevel4(self):
        pass

    def exprLevel5(self):
        pass

    def exprLevel6(self):
        pass