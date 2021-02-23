import caelex, sys, os, caeparser, caei, caeerr

class ArgumentParser:
    def __init__(self, arguments: list):
        self.arguments = arguments[1:]

        self.parse_arguments()

    def parse_arguments(self):
        # print(self.arguments)
        if len(self.arguments) >= 1:
            filename = self.arguments[0]
            if os.path.exists(filename):
                if not os.path.isfile(filename):
                    self.throw_error(f"{filename} is not a file", True)
                else:
                    with open(filename, "r") as source_code_reader:
                        script = source_code_reader.read()
            else:
                self.throw_error(f"{filename} does not exist", True)
        else:
            print("Welcome to Caesium interactive shell")
            get_console_input = True

            while get_console_input:
                try:
                    user_input = str(input("> "))
                except KeyboardInterrupt:
                    self.throw_error("KeyboardInterrupt", False)
                    continue

                if user_input == ".exit":
                    get_console_input = False
                elif user_input == "clear" or user_input == "cls" or user_input == "clean":
                    os.system("cls" if os.name != "posix" else "clear")
                elif user_input.rstrip().lstrip() == "":
                    continue
                else:
                    lexer = caelex.CaeLexer(user_input)
                    lexed_tokens = lexer.lex()

                    parser = caeparser.CaeParser(lexed_tokens)
                    parser.parse()

                    interp = caei.CaeInterpreter()
                    behavior = interp.visit(parser.ast[0])

                    print(behavior)

    def throw_error(self, error_message: str, exit: bool):
        print(f"\n{error_message}")
        
        if exit:sys.exit()

if __name__ == '__main__':
    argument_parser = ArgumentParser(sys.argv)