import sys, os
from run.caelex import Lexer
from run.caeparser import Parser

try: 
    sys.argv[1]
except:
    while True:
        code: str = input("> ")
        print(code)
        lexer: Lexer = Lexer(code)
        tokens: list = lexer.lex()
        parser: Parser = Parser(tokens)
        AST = parser.parse()
        print(AST)
else:
    code: str = ""
    if os.path.exists(sys.argv[1]) and os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], "r") as file:
            code = file.read()
        print(code)
        lexer: Lexer = Lexer(code)
        tokens: list = lexer.lex()
        parser: Parser = Parser(tokens)
        AST = parser.parse()
        print(AST)
    else:
        print("Please enter a valid file.")
