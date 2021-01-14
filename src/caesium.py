import caelex, sys, os

try:
    with open(str(sys.argv[1])) as fn:
        script = fn.read()
except IndexError:
    print("Welcome to Caesium interactive shell!")
    while True:
        a = input('> ')
        lexer = caelex.CaeLexer(a)

        lexed = lexer.lex()
        if a == ".exit":
            break
        elif a == "clear" or a == "cls":
            os.system("cls" if os.name != "posix" else "clear")
        else:
            print(lexed)