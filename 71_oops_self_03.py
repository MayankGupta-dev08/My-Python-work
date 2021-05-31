'''Understanding self'''

class Company:
    company = "GOOGLE"
    location = "Banglore"
    def empDetails(self):
        print(f"Employee Name: {self.name} and his Salary is {self.salary}. He is current Location is {self.location}.\n")

emp = Company() #Object Instantiation
print("")
print(Company.company)
num_emp = int(input("Enter no. of employees in the company: "))
for i in range(num_emp):
    emp.name = input("Enter your name: ")
    emp.salary = int(input("Enter your salary: "))
    emp.empDetails()
    print(emp.__dict__, "\n") # Prinitng dictionary for each instance of the object. Here, we can see that only name and salary are being in dictionary, as they are instance attribute of object emp, where as company and location are class attributes.

print("")
print(emp.__dict__) # Prinitng dictionary for only last instance of the object.
# print(Company.__dict__) # Not used, it's possible but not used.