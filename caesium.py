import sys, os
import caelex

while True:
    code = input("> ")
    print(code)
    lexer: caelex.Lexer = caelex.Lexer(code)
    tokens: list = lexer.lex()
    print(tokens)