'''Some other dunder methods
__str__ helps in printing the desired thing just by using print(object)

'''

class Number:
    def __init__(self, num):
        self.num = num
    
    def __add__(self,num2): # Here, self is instance of n1 and num2 is an instance of n2 and both will have their own num values. 
        print("Let's add")
        return self.num + num2.num
    
    def __str__(self):
        return f"The number in n1 is {self.num}"
        # print(f"The number in n1 is {self.num}") 
        # By writing this we could simply call the function __str__ by n1.__str__() and get the same result.
    
    def __len__(self):
        return 1

n1 = Number(2)
n2 = Number(4)
sum = n1+n2 #Adding the num of the two objects using '+' operator overloading, as both are objects and + will call __add_ automatically.
print(sum)
print(n1)
print(len(n1))
