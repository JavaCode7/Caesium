class CaeError:
    def __init__(self, error: str=""):
        self.error: str = error

    def throw(self):
        print("\033[91m" + self.error + "\033[0m")
        quit()