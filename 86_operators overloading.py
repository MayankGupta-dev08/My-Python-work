'''Using Operator Overloading'''
class Number:
    def __init__(self, num):
        self.num = num
    
    def __add__(self,num2): # Here, self is instance of n1 and num2 is an instance of n2 and both will have their own num values. 
        print("Let's add")
        return self.num + num2.num
    
n1 = Number(2)
n2 = Number(4)
sum = n1+n2 #Adding the num of the two objects using '+' operator overloading, as both are objects and + will call __add_ automatically.
print(sum)
n3 =5
n4=6
sum2 = n3+n4 #simple addition of two integers.
print("Sum2 is: ", sum2)

'''Doing above thing without overloading'''
# class Number:
#     def __init__(self, num):
#         self.num = num
        
#     def add(self,num2):
#         print(f"Let's add: {self.num + num2.num}")
      
# n1 = Number(2)
# n2 = Number(4)
# sum = n1.add(n2)

'''Doing above thing without overloading in another way.'''
# class Number:
#     def __init__(self, num):
#         self.num = num
        
#     def add(self,num2):
#         print(f"Let's add: {self.num + num2}")
        
# n1 = Number(2)
# n2 = Number(4)
# sum = n1.add(n2.num)