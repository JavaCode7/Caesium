class CaeToken():

    def __init__(self, _type: str = "", value = ""):
        self.type: str = _type
        self.value = value
    
    def __repr__(self):
        return f"Token of type {self.type} and value '{self.value}'"