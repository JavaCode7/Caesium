import caelex, sys, os, caeparser, caei, caeerr

class ArgumentParser:
    def __init__(self, arguments):
        self.arguments = arguments[1:]

        self.parse_arguments()

    def parse_arguments(self):
        # print(self.arguments)
        if len(self.arguments) >= 1:
            filename = self.arguments[0]
            if os.path.exists(filename):
                if not os.path.isfile(filename):
                    self.throw_error(f"{filename} is not a file")
                else:
                    pass
            else:
                self.throw_error(f"{filename} does not exists")

    def throw_error(self, error_message):
        print(f"ERROR : {error_message}")
        sys.exit()


# try:
#     with open(str(sys.argv[1])) as fn:
        
#         script = fn.read()
# except IndexError:
#     print("Welcome to Caesium interactive shell!")
#     while True:
#         try:
#             a = input('> ')
#         except KeyboardInterrupt:
#             print("\n\033[3m KeyboardInterrupt \033[0m")
#             continue
#         if a == ".exit":
#             break
#         elif a == "clear" or a == "cls" or a == "clean":
#             os.system("cls" if os.name != "posix" else "clear")
#         else:
#             lexer = caelex.CaeLexer(a)

#             lexed = lexer.lex()

#             print(lexed)

#             parser = caeparser.CaeParser(lexed)

#             parser.parse()

#             print(parser.ast)

#             interp = caei.CaeInterpreter()

#             behavior = interp.visit(parser.ast[0])

#             print(behavior)
#             print(type(behavior))
if __name__ == '__main__':
    argument_parser = ArgumentParser(sys.argv)