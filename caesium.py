import sys, os
import caelex

while True:
    code = input("> ")
    print(code)
    lexer: caelex.Lexer = caelex.Lexer(code)
    lexer.lex()