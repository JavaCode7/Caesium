import caetoken, caenodes

class CaeParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current: caetoken.CaeToken = None
        self.index = -1
        self.advance()

    def advance(self, amount: int = 1):
        self.index += amount
        try:
            self.current = self.tokens[self.index]
        except IndexError:
            self.current = "cae-end-of-file"

    def parse(self):
        while self.current != "cae-end-of-file":
            self.expr()
            self.advance()

    def expr(self):
        if self.current.type == "INT" or self.current.type = "FLOAT"