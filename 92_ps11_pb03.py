class Employee:
    c_name = "ASUS"
    e_name = "Bharat"
    basicSalary = 800000
    increment = 5000

    def __init__(self):
        print(f"{self.e_name} is working in {self.c_name}.")
        print(f"He is having Basic as Rs. {self.basicSalary}/- & yearly increment of Rs. {self.increment}/-")

    @classmethod
    def changeIncrement(cls, incre):
        cls.increment = incre
        print(f"Revised Increment: {cls.increment}")

    @property
    def SalaryAfterIncrement(self):
        return self.basicSalary + self.increment
    
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, val):
        self.increment = val - self.basicSalary

emp1 = Employee()
print(emp1.SalaryAfterIncrement)
emp1.changeIncrement(10000)
print(emp1.SalaryAfterIncrement)
emp1.SalaryAfterIncrement = 820000
print("After an year: ", emp1.SalaryAfterIncrement)
print("BasicSalary: ", emp1.basicSalary)
print("Increment: ", emp1.increment)