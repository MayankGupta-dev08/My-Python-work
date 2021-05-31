'''' Name of the class is written in PascalCase format,

PascalCase: NameClass, EmployeeName  --> used for class (generally)
camelCase: isNumeric, isFloatOrInt  --> used for functions (not necessarily)

'''

# OOPS Example1
class NumClass: #Class Definition, Name of Class is NumClass
    def sum(self): #Member fuction of class NumClass
        return self.a + self.b

num = NumClass() #creating an object of the NumClass as num. 
num.a = 12 #Data member of NumClass
num.b = 42 #Data member of NumClass
result = num.sum() #Calling sum which is a member fuction of NumClass, as their is no constructor (def __init__(self):) in this class, so after calling this class will do some work using sum fuction.
print("Sum: ",result,"\n")

# OOPS Example2
class Railway:
    formType = "Railway Form"
    def printData(self):
        print(f"Name: {self.name}")
        print(f"Train: {self.train}")
        print(f"Date: {self.date}")

mayankApplication = Railway()
mayankApplication.name = "Mayank"
mayankApplication.train = "Rajdhani Express"
mayankApplication.date = "24 May 2021"
mayankApplication.printData()