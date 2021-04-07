class FuncDef:
    def __init__(self, return_type: str, name: str, body: any):
        self.return_type: str = return_type
        self.name: str = name
        self.body: any = body

    def __repr__(self):
        return f"({self.return_type} func {self.name} [{self.body}])"