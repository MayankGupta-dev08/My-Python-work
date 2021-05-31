'''Property Decorator - @property
a.k.a - getter method'''
# .

class Employee:
    name = "Bharat Gas"
    salary = 5600
    salaryBonus = 500
    # salaryTotal = 6100 #We don't want it to be permanent.
    
    def ChangeSalaryBonus(self, bonus):
        self.__class__.salaryBonus = bonus
        
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus
        # Here, we have made a function which works as attributes and retuns the total salary after computing it.
        # We could have made this just a function without using @property, then we would have to call it like a normal function to do its work. But instead we have made this an attribute so it would work like one.
    
e = Employee()
print(e.totalSalary)
e.ChangeSalaryBonus(400)
print(e.totalSalary)