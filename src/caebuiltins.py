import caeerr

class Value:
    
    def __init__(self, value):
        self.val = value

    def mul(self, **args):
        caeerr.throw(caeerr.UnsupportedOpError, "Unsupported Operation")

    def div(self, **args):
        caeerr.throw(caeerr.UnsupportedOpError, "Unsupported Operation")

    def plus(self, **args):
        caeerr.throw(caeerr.UnsupportedOpError, "Unsupported Operation")

    def minus(self, **args):
        caeerr.throw(caeerr.UnsupportedOpError, "Unsupported Operation")
    
class Number(Value):

    def __init__(self, num):
        super().__init__(num)

    def mul(self, right):
        return self.num * right.num
    
    def div(self, right):
        return self.num / right.num

class Int(Number):
    def __init__(self, num):
        self.num = int(num)
        super().__init__(self.num)

    def __repr__(self):
        return f"{self.num}"

class Float(Number):
    def __init__(self, num):
        self.num = float(num)
        super().__init__(self.num)
    
    def __repr__(self):
        return f"{self.num}"
