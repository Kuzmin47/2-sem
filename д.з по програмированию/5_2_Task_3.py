class ListMath:
    def __init__(self, lst=None):
        self.lst_math = []
        if lst is not None:
            self.lst_math = [x for x in lst if isinstance(x, (int, float)) and not isinstance(x, bool)]
    
    def __add__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return ListMath([x + other for x in self.lst_math])
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __iadd__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        self.lst_math = [x + other for x in self.lst_math]
        return self
    
    def __sub__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return ListMath([x - other for x in self.lst_math])
    
    def __rsub__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return ListMath([other - x for x in self.lst_math])
    
    def __isub__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        self.lst_math = [x - other for x in self.lst_math]
        return self
    
    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return ListMath([x * other for x in self.lst_math])
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __imul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        self.lst_math = [x * other for x in self.lst_math]
        return self
    
    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return ListMath([x / other for x in self.lst_math])
    
    def __rtruediv__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return ListMath([other / x for x in self.lst_math])
    
    def __itruediv__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        self.lst_math = [x / other for x in self.lst_math]
        return self