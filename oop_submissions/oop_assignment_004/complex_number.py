import math
class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self._real_part = real_part
        self._imaginary_part = imaginary_part
        
        if type(self._real_part) == str and type(self._imaginary_part) != str:
            raise ValueError("Invalid value for real part")
            
        if (self._imaginary_part.__class__) == str and (self._real_part.__class__) != str:
            raise ValueError("Invalid value for imaginary part")
            
        if type(self._real_part) and type(self._imaginary_part) == str:
            raise ValueError("Invalid value for real and imaginary part")
            
    @property
    def real_part(self):
        return self._real_part
        
    @property
    def imaginary_part(self):
        return self._imaginary_part
    
    def __str__(self):
        return f"{self._real_part}{self._imaginary_part:+}i"
        
    def conjugate(self):
        return self.__class__(self._real_part,-self._imaginary_part)
    
    def __add__(self, other):
        return self.__class__(self._real_part + other._real_part,self._imaginary_part + other._imaginary_part)
        
    def __sub__(self, other):
        return self.__class__(self._real_part - other._real_part,self._imaginary_part - other._imaginary_part)
    
    def __mul__(self, other):
        real_part = (self._real_part * other._real_part) - (self._imaginary_part * other._imaginary_part)
        imaginary_part = (self._real_part * other._imaginary_part) + (self._imaginary_part * other._real_part)
        return self.__class__(real_part, imaginary_part)
    
    def __truediv__(self,other):
        r = float(other._real_part**2 + other._imaginary_part**2)
        return ComplexNumber((self._real_part * other._real_part + self._imaginary_part * other._imaginary_part)/r,
        (self._imaginary_part * other._real_part - self._real_part * other._imaginary_part)/r)
            
    def __abs__(self):
        absolute = math.sqrt(self._real_part**2 + self._imaginary_part**2)
        return round(absolute,3)
        
    def __eq__(self,other):
        if self._real_part == other._real_part and self._imaginary_part == other._imaginary_part:
            return True
        else:
            return False
        
"""
if other._real_part and other._imaginary_part == 0:
            raise ZeroDivisionError("division by zero")
        else:
            if self._imaginary_part or other._imaginary_part < 0:
                self._real_part = -(self._real_part)
                self._imaginary_part = -(self._imaginary_part)
                other._real_part = -(other._real_part)
                other._imaginary_part = -(other._imaginary_part)
                r = float(other._real_part**2 + other._imaginary_part**2)
                return ComplexNumber((self._real_part * other._real_part + self._imaginary_part * other._imaginary_part)/r,
                (self._imaginary_part * other._real_part - self._real_part * other._imaginary_part)/r)
"""