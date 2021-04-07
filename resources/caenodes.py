class ProgramNode:
    def __init__(self, body: any):
        self.body: any = body

    def __repr__(self):
        return f"({self.body})"