'''Changing Class Attributes'''

# Method 1 to change a class attribute  --> ClassName.attribute = changeValue.
# class Employee:
#     name = "Logitech"
#     eCode = 1513131
#     Location = "Delhi"
    
#     def __init__(self):
#         print(self.eCode)

# e = Employee()
# Employee.eCode = 64664
# print(Employee.eCode)
# e2 = Employee()
# print(e2.eCode)


# Method 2 to change a class attribute --> Using (dunder) __class__.
# class Employee:
#     name = "Logitech"
#     eCode = 1513131
#     Location = "Delhi"
    
#     def changeECode(self, ec):
#         self.__class__.eCode = ec
    
# e = Employee()
# print(e.eCode)
# e.changeECode(546451)
# print(e.eCode)
# print(Employee.eCode)

# Method 3 to change a class attribute --> Using Class method @classmethod and cls in place of self.
class Employee:
    name = "Logitech"
    eCode = 1513131
    Location = "Delhi"
    
    @classmethod
    def changeECode(cls, ec):
        cls.eCode = ec
        cls.Location = "Noida"
    
e = Employee()
print(e.eCode)
e.changeECode(546451)
print(e.eCode)
print(Employee.eCode)
print(e.Location)
print(Employee.Location)

