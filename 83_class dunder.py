'''CLass dunder - __class__'''
# Method 2 to change a class attribute --> Using (dunder) __class__.
# Class bender (__class__) is preferred when we don't want to completely make a function which changes the class attributes rather we want to change only a single or few of class attributes and not all in that function using cls and @classmethod.

class Employee:
    name = "Logitech"
    eCode = 1513131
    Location = "Delhi"
    
    def changeECode(self, ec):
        self.__class__.eCode = ec #Changing permanently.
        self.Location = "Noida" #Changing only for that instance or object.
    
e = Employee()
print(e.eCode)
e.changeECode(546451)
print(e.eCode)
print(Employee.eCode)
print(e.Location)
print(Employee.Location)