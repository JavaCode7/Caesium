from resources.caetoken import Token
from resources.caenodes import *
from error.caeerr import CaeError

class Parser:
    def __init__(self, tokens: list):
        self.tokens: list = tokens
        self.index: int = -1
        self.current: Token = None

    def parse(self) -> ProgramNode:
        parsed = self.program()
        return parsed

    def advance(self, amount: int = 1):
        try:
            self.index += amount
            self.current = self.tokens[self.index]
        except IndexError:
            self.index -= amount
            self.current = Token("EOF", "<EOF>")

    def program(self) -> ProgramNode:
        program: list = []
        while not self.current.matches("EOF", "<EOF>"):
            program.append(self.statement())
        return ProgramNode(program)

    def statement(self):
        pass