import caetoken, caenodes, caeerr

class CaeParser:
    def __init__(self, tokens):
        self.ast: list = []
        self.tokens: list = tokens
        self.current: caetoken.CaeToken = None
        self.index: int = 0
        self.current = self.tokens[self.index]
        self.signals: dict = {"num": True}
        self.highest: function = self.exprLevel5

    def advance(self, amount: int = 1):
        self.index += amount
        try:
            self.current = self.tokens[self.index]
        except IndexError:
            self.current = "cae-end-of-file"

    def parse(self):
        while self.current != "cae-end-of-file":
            self.ast.append(self.highest())
            self.advance()
        for i in range(len(self.ast) - 1, -1, -1):
            if self.ast[i] == None:
                del self.ast[i]

    #? Literals
    def exprLevel1(self):
        if self.current.type in ("STRING", "CHARACTER"):
            return caenodes.StringNode(str(self.current.value)) if self.current.type == "STRING" else caenodes.CharNode(str(self.current.value))
        if not self.signals["num"]:
            self.advance(-1)
        if self.current.type in ("INTEGER", "FLOAT"):
            return caenodes.NumberNode(str(self.current.value))
        else:
            caeerr.throw(caeerr._SyntaxError, "Expected an int, float, string or char")


    #? Parentheses
    def exprLevel2(self):
        pass

    #? Pow
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
                        right = self.highest()
                        return caenodes.BinOpNode(left, op, right)

        elif self.current.type in ("STRING", "CHARACTER"):
            self.advance(2)
            if self.current == "cae-end-of-file":
                self.advance(-2)
                return self.exprLevel1()
            else:
                self.signals["num"]: bool == False
                self.advance(-2)
                left = self.exprLevel1()
                self.advance()
                if self.current.type in ("MUL"):
                    op = self.current.value
                    self.advance()
                    if self.current.type in ("INTEGER", "FLOAT"):
                        right = self.highest()
                        return caenodes.BinOpNode(left, op, right)
        else:
            caeerr.throw(caeerr._SyntaxError, "Expected an int, float, string or char")

    #? Plus/Minus
    def exprLevel5(self):
        if self.current.type in ("INTEGER", "FLOAT"):
            self.advance(2)
            if self.current == "cae-end-of-file":
                self.advance(-2)
                return self.exprLevel1()
            else:
                self.signals["num"]: bool == False
                self.advance(-2)
                left = self.exprLevel4()
                self.advance()
                if self.current != "cae-end-of-file":
                    self.advance(-1)
                    if self.current.type in ("PLUS", "MINUS"):
                        op = self.current.value
                        self.advance()
                        if self.current.type in ("INTEGER", "FLOAT"):
                            right = self.exprLevel4()
                            return caenodes.BinOpNode(left, op, right)
                    elif self.current.type in ("MUL", "DIV"):
                        self.advance(-1)
                        return self.exprLevel4()
                else:
                    return left

        elif self.current.type in ("STRING", "CHARACTER"):
            self.advance(2)
            if self.current == "cae-end-of-file":
                self.advance(-2)
                return self.exprLevel1()
            else:
                self.signals["num"]: bool == False
                self.advance(-2)
                left = self.exprLevel1()
                self.advance()
                if self.current.type in ("PLUS"):
                    op = self.current.value
                    self.advance()
                    if self.current.type in ("INTEGER", "FLOAT"):
                        right = self.highest()
                        return caenodes.BinOpNode(left, op, right)
                elif self.current.type in ("MUL"):
                    self.advance(-1)
                    return self.exprLevel4()
        else:
            caeerr.throw(caeerr._SyntaxError, "Expected an int, float, string or char")

    #? Base
    def exprLevel6(self):
        pass