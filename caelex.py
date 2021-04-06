from resources.caetoken import Token
from resources.caedata import keywords
from error.caeerr import CaeError
from os import linesep

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
            elif self.current == " ":
                self.tokens.append(Token("WS", self.current))
                self.advance()
            elif self.current in "_QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioasdfghjklzxcvbnmp":
                ident: str = self.current
                self.advance()
                while self.current in "_QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioasdfghjklzxcvbnmp0123456789":
                    ident += self.current
                    self.advance()
                self.tokens.append(Token("ID", ident)) if ident not in keywords else self.tokens.append(Token("KW", ident))
            elif self.current == "(":
                self.tokens.append(Token("LPAREN", self.current))
                self.advance()
            elif self.current == ")":
                self.tokens.append(Token("RPAREN", self.current))
                self.advance()
            elif self.current == "{":
                self.tokens.append(Token("LBRACE", self.current))
                self.advance()
            elif self.current == "}":
                self.tokens.append(Token("RBRACE", self.current))
                self.advance()
            elif self.current == ".":
                self.tokens.append(Token("DOT", self.current))
                self.advance()
            elif self.current == "\n":
                self.tokens.append(Token("WS", self.current))
                self.advance()
            else:
                CaeError(f"Illegal Character `{self.current}`").throw()
        return self.tokens