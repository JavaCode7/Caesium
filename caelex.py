from resources.caetoken import Token

class Lexer:
    def __init__(self, code: str):
        self.code: str = code
        self.index: int = -1
        self.current: str = ""
        self.tokens: list = []
        self.advance()

    def advance(self, amount: int = 1):
        try:
            self.index += 1
            self.current = self.code[self.index]
        except IndexError:
            self.index -= 1
            self.current = "<EOF>"

    def lex(self) -> list:
        while self.current != "<EOF>":
            if self.current == "\"":
                self.advance()
                string: str = self.current
                self.advance()
                while self.current != "\"":
                    string += self.current
                    self.advance()
                self.advance()
                self.tokens.append(Token("STR", string))
            elif self.current in "_QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioasdfghjklzxcvbnmp":
                ident: str = self.current
                self.advance()
                while self.current in "_QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioasdfghjklzxcvbnmp0123456789":
                    ident += self.current
                    self.advance()
                self.tokens.append(Token("ID", ident))
        return self.tokens