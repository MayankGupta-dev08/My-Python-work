'''Addition and Multiplication of two complex No.'''

class ComplesNum:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def __add__(self, c):
        return ComplesNum(self.real + c.real, self.imag + c.imag)
        # Here, actually a another object of class ComplexNum is being created and returned.
    
    def __mul__(self, c):
        # (a+bi)*(c+di) = (ac-bd) + (ad+bc)i 
        return ComplesNum(((self.real*c.real)-(self.imag*c.imag)), ((self.real*c.imag)+(self.imag*c.real)))
    
    def __str__(self):
        if self.imag>=0:        
            return f"{self.real} + {self.imag}i"
        else:        
            return f"{self.real} {self.imag}i" #No need to add '-' symbol in b/w as it will be come twice if added.

c1 = ComplesNum(3,-4)
print("1st Complex Number: ", c1)
c2 = ComplesNum(4,5)
print("2nd Complex Number: ", c2)
print("Sum of the above complex numbers", c1+c2)
# This could have also be written as, we are directly trying to add two objects using dunder __add__
# c3 = c1+c2
# print("Sum of the above complex numbers", c3)
print("Multiplication of the above complex numbers", c1*c2)