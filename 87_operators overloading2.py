'''Some more examples of Operators Overloading'''
class Number:
    def __init__(self, num):
        self.num = num
    
    def __add__(self,num2): # Here, self is instance of n1 and num2 is an instance of n2 and both will have their own num values. 
        print("Let's add")
        return self.num + num2.num
    
    def __mul__(self,num2): 
        print("Let's multiply")
        return self.num * num2.num
    
    def __sub__(self,num2): 
        print("Let's subtract")
        return self.num - num2.num

    def __truediv__(self,num2): 
        print("Let's divide")
        return self.num / num2.num
 
    def __floordiv__(self,num2): 
        print("Let's divide")
        return self.num // num2.num
    
n1 = Number(4)
n2 = Number(2)
sum = n1+n2 #Adding the num of the two objects using '+' operator overloading, as both are objects and + will call __add_ automatically.
print(sum)
mult = n1*n2
print(mult)
sub = n1-n2
print(sub)
tdiv = n1/n2
print("tdiv / : ",tdiv)
fdiv = n1//n2
print("fdiv // : ", fdiv)