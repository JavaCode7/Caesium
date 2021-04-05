class Lexer:
    def __init__(self, code: str):
        self.code: str = code
        self.index: int = -1
        self.current: str = ""
        self.tokens = []
        self.advance()

    def advance(self, amount: int = 1):
        try:
            self.index += 1
            self.current = self.code[self.index]
        except IndexError:
            self.index -= 1
            self.current = "<EOF>"

    def lex(self):
        while self.current != "<EOF>":
            pass