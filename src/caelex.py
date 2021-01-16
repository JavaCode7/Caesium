import re, caeerr, caerules, caetoken

class CaeLexer:
    
    def __init__(self, text: str, tokens: list = None):
        self.text: str = text
        self.index: int = -1
        self.current: any = None
        self.loc: int = 1
        self.tokens: list = tokens if tokens else []
        self.advance()

    def advance(self, amount: int = 1):
        self.index += amount
        if self.index < len(self.text):
            self.current = self.text[self.index]
        else:
            self.current = "cae-end-of-file"

    def lex(self):
        while self.current != "cae-end-of-file":
            #? Comment
            if self.current == "@":
                self.advance()
                if self.current == "#":
                    self.advance(2)
                    while self.current != "#":
                        self.advance()
                    self.advance()
            #? Str/Char
            elif self.current in "\"'`":
                string_start: str = self.current
                self.advance()
                string: str = ""
                while self.current != string_start:
                    string += self.current
                    self.advance()
                if string_start == "'":
                    if len(string) <= 1:
                        self.tokens.append(caetoken.CaeToken("CHARACTER", string))
                    else:
                        caeerr.throw(caeerr.CharError, "Char string should have length 1", self.loc)
                else:
                    self.tokens.append(caetoken.CaeToken("STRING", string))
                self.advance()
                self.advance(-1)
            #? Newline
            elif self.current == "\n":
                lines = "\n"
                while self.current in "\n":
                    lines += self.current
                    self.loc += 1
                    self.advance()
                self.tokens.append(caetoken.CaeToken("NEWLINE", lines))
                self.advance(-1)
            #? Whitespace/Indent
            elif self.current == " ":
                spaces = " "
                self.advance()
                while self.current == " ":
                    spaces += " "
                    self.advance()
                self.advance(-1)
                self.tokens.append(caetoken.CaeToken("WHITESPACE", spaces)) if int(len(spaces)) not in caerules.CaeRules.INDENT_SIZES else self.tokens.append(caetoken.CaeToken("INDENT", spaces))
            #? Tab
            elif self.current == "\t":
                tabs = "\t"
                while self.current == "\t":
                    tabs += "\t"
                    self.advance()
                self.tokens.append(caetoken.CaeToken("INDENT", tabs))
            #? Int/Float
            elif re.match(r"[0-9]", self.current):
                num: str = str(self.current)
                dot_count = 0
                self.advance()
                while self.current in "1234567890.":
                    if self.current == ".": dot_count += 1;
                    if dot_count > 1: caeerr.throw(caeerr.DotError, "Only 1 dot allowed in float", self.loc)
                    num += self.current
                    self.advance()
                self.advance(-1)
                self.tokens.append(caetoken.CaeToken("FLOAT", float(num))) if dot_count == 1 else self.tokens.append(caetoken.CaeToken("INTEGER", int(num)))
            #? Identifier/Keyword
            elif self.current in "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX":
                ident: str = str(self.current)
                self.advance()
                while self.current in "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
                    ident += self.current
                    self.advance()
                self.tokens.append(caetoken.CaeToken("IDENTIFIER", str(ident))) if str(ident) not in caerules.CaeRules.KEYWORDS else self.tokens.append(caetoken.CaeToken("KEYWORD", str(ident)))
                self.advance(-1)
            #? Dot
            elif self.current == ".":
                self.tokens.append(caetoken.CaeToken("DOT", "."))
            #? Lbrace
            elif self.current == "{":
                self.tokens.append(caetoken.CaeToken("LBRACE", "{"))
            #? Rbrace
            elif self.current == "}":
                self.tokens.append(caetoken.CaeToken("RBRACE", "}"))
            #? Semi
            elif self.current == ";":
                self.tokens.append(caetoken.CaeToken("SEMI", ";"))
            #? Lparen
            elif self.current == "(":
                self.tokens.append(caetoken.CaeToken("LPAREN", "("))
            #? Rparen
            elif self.current == ")":
                self.tokens.append(caetoken.CaeToken("RPAREN", ")"))
            #? Plus
            elif self.current == "+":
                self.tokens.append(caetoken.CaeToken("PLUS", "+"))
            #? Minus
            elif self.current == "-":
                self.tokens.append(caetoken.CaeToken("MINUS", "-"))
            #? Multiply
            elif self.current == "*":
                self.tokens.append(caetoken.CaeToken("MUL", "*"))
            #? Divide
            elif self.current == "/":
                self.tokens.append(caetoken.CaeToken("DIV", "/"))
            #? Exp
            elif self.current == "^":
                self.tokens.append(caetoken.CaeToken("POW", "^"))
            #? Eq
            elif self.current == "=":
                self.tokens.append(caetoken.CaeToken("EQ", "="))
            #! Illegal Char Err
            elif self.current != "cae-end-of-file":
                caeerr.throw(caeerr.IllegalCharError, f"Illegal Char `{self.current}`", self.loc)
            self.advance()
        return self.tokens