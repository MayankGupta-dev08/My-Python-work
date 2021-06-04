'''Setter Decorator - @name.setter
Generally, getter and setter are used simultaneously.
@property - for an attribute.
@NAME.setter - uses the same function for which @property was used, to set its value as constant'''


# This will show why we need to use property decorator and setter decorator.
class Employee:
    name = "Bharat Gas"
    salary = 5600
    salaryBonus = 500
    salaryTotal = salary + salaryBonus
    
e1= Employee()
print(e1.salary)        # 5600
print(e1.salaryTotal)   # 6100
Employee.salaryBonus = 400
e2= Employee()          
print(e2.salaryBonus)   # 400
print(e2.salaryTotal)   # 6100

# NOTE - So from the above example it's clear that salaryTotal is computed only once as it is a class variable and although salaryBonus which is a class variable is changed using Employee.salaryBonus = 400, then also it's not changed.
# NOTE - So, we can't have variables which are dynamic as class variable or instance variable in constructor but we can have them as instance variable in some class method/function or if we want it to be a property/attribute than we can use property decorator.

# Example for setter.
class Employee:
    name = "Bharat Gas"
    salary = 5600
    salaryBonus = 500
    # salaryTotal = 6100 #We don't want it to be permanent.
    
    def ChangeSalaryBonus(self, bonus):
        self.__class__.salaryBonus = bonus
        print(self.salaryBonus)
        
    @property  #Makes totalSalary an attribute.
    def totalSalary(self):
        return self.salary + self.salaryBonus
        # Here, it is GETTING the value of totalSalary on the basis of salary and bonus. 
    
    @totalSalary.setter  #Used on same function, Uses totalSalary as an attribute whose value is fixed(set).
    def totalSalary(self, val): # val contains the value of totalSalary.
        self.salaryBonus = val - self.salary
    
e = Employee()
print(e.salary)  
print(e.salaryBonus)
print(e.totalSalary)
e.ChangeSalaryBonus(400)
print(e.totalSalary)
e.totalSalary = 5800
print(e.totalSalary)
print(e.salary)
print(e.salaryBonus)

'''OUTPUT'''
# 5600
# 500
# 6100
# 400
# 6000
# 5800
# 5600
# 200