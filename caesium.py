import sys, os
import caelex

try: 
    sys.argv[1]
except:
    while True:
        code: str = input("> ")
        print(code)
        lexer: caelex.Lexer = caelex.Lexer(code)
        tokens: list = lexer.lex()
        print(tokens)
else:
    code: str = ""
    if os.path.exists(sys.argv[1]) and os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], "r") as file:
            code = file.read()
        print(code)
        lexer: caelex.Lexer = caelex.Lexer(code)
        tokens: list = lexer.lex()
        print(tokens)
    else:
        print("Please enter a valid file.")
