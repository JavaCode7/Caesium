class Token:
    def __init__(self, _type: str, value: any):
        self.type = _type
        self.value = value

    def matches(self, _type: str, value: any):
        return self.type == _type and self.value == value
    
    def __repr__(self) -> str:
        return f"({self.type}:{self.value})"