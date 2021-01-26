class CaeError:

    def __init__(self, _type, reason: str = "", loc: int = 1):
        self.type = _type
        self.reason = reason
        self.loc = loc
    
    def __str__(self):
        return f'{repr(self.type)}{str(self.reason)}'

    def __repr__(self):
        return f"Error at line {self.loc}: "
        
class LexerError(CaeError):

    def __init__(self, _type, reason: str = "", loc: int = 1):
        super().__init__(self, reason, loc)

    def __repr__(self):
        return f"Lex Error at line {self.loc}: "

class StringError(LexerError):

    def __init__(self, _type, reason: str = "", loc: int = 1):
        super().__init__(self, reason, loc)

    def __repr__(self):
        return f"String Error at line {self.loc}: "

class CharError(StringError):
    def __init__(self, reason: str = "", loc: int = 1):
        super().__init__(self, reason, loc)

    def __repr__(self):
        return f"Char Error at line {self.loc}: "

class DotError(LexerError):

    def __init__(self, reason: str = "", loc: int = 1):
        super().__init__(self, reason, loc)

    def __repr__(self):
        return f"Dot Error at line {self.loc}: "

class IllegalCharError(LexerError):

    def __init__(self, reason: str = "", loc: int = 1):
        super().__init__(self, reason, loc)

    def __repr__(self):
        return f"Illegal Char Error at line {self.loc}: "

class ExpectedCharError(LexerError):

    def __init__(self, reason: str = "", loc: int = 1):
        super().__init__(self, reason, loc)

    def __repr__(self):
        return f"Expected Char Error at line {self.loc}: "

def throw(_type = CaeError, error: str = "", loc: int = 1):
    to_print: CaeError = _type(error, loc)
    print(f"\033[31m{str(to_print)}\033[0m")
    quit()

def nonterminalthrow(_type = CaeError, _subtype = LexerError, error: str = "", loc: int = 1):
    to_print: CaeError = _type(_subtype, error, loc)
    print(f"\033[31m{str(to_print)}\033[0m")
    quit()