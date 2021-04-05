class Token:
    def __init__(self, _type: str, value: any):
        self.type = _type
        self.value = value
    
    def __repr__(self) -> str:
        return f"({self.type}:{self.value})"