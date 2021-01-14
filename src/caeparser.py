import caetoken, caenodes

class CaeParser:
    def __init__(self, tokens):
        self.tokens: list = tokens
        self.current: caetoken.CaeToken = None
        self.index: int = -1
        self.advance()

    def advance(self, amount: int = 1):
        self.index += amount
        try:
            self.current = self.tokens[self.index]
        except IndexError:
            self.current = "cae-end-of-file"

    def parse(self):
        while self.current != "cae-end-of-file":
            self.exprLevel3()
            self.advance()

    def exprLevel1(self):
        if self.current.type == "INT" or self.current.type == "FLOAT":
            num: float = float(self.current.value)

    def exprLevel2(self):
        pass

    def exprLevel3(self):
        pass

    def exprLevel4(self):
        pass

