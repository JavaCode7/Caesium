import caelex, sys, os, caeparser

try:
    with open(str(sys.argv[1])) as fn:
        script = fn.read()
except IndexError:
    print("Welcome to Caesium interactive shell!")
    while True:
        try:
            a = input('> ')
        except KeyboardInterrupt:
            print("\n\033[3m KeyboardInterrupt \033[0m")
            continue
        if a == ".exit":
            break
        elif a == "clear" or a == "cls" or a == "clean":
            os.system("cls" if os.name != "posix" else "clear")
        else:
            lexer = caelex.CaeLexer(a)

            lexed = lexer.lex()

            parser = caeparser.CaeParser(lexed)

            parser.parse()

            print(parser.ast)