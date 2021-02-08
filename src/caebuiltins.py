import caeerr, caenodes

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
        try:
            return self.num / right.num
        except ZeroDivisionError:
            caeerr.throw(caeerr._ZeroDivisionError, "Zero Division")
    
    def plus(self, right):
        return self.num + right.num

    def minus(self, right):
        return self.num - right.num

class Int(Number):
    def __init__(self, num):
        self.num = int(num)
        super().__init__(self.num)

    def __repr__(self):
        return f"{self.num}"

class Float(Number):
    def __init__(self, num):
        self.num = float(num) if not isinstance(num, caenodes.NumberNode) else float(num.num)
        super().__init__(self.num)
    
    def __repr__(self):
        return f"{self.num}"

class String(Value):
    def __init__(self, string):
        self.string = str(string)
        super().__init__(self.string)

    def mul(self, right):
        return self.string * right.num

    def plus(self, right):
        return self.string + right.string

    def __repr__(self):
        return f"{self.string}"

class Char(String):
    def __init__(self, string):
        self.string = str(string)
        super().__init__(self.string)

    def __repr__(self):
        return f"{self.string}"
