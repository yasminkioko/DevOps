import math

class operations:

    def sum(self, x,y):
        return x+y

    def subtraction(self, x,y):
        return x-y

    def muntiplication(self, x,y):
        return x*y

    def division(self, x,y):
        return x/y if y != 0 else None
    
    def pow(x,y):
        return math.pow(x,y)

    def sqrt(x):
        return math.sqrt(x)
    
    def cos(x):
        return math.acos(x)
