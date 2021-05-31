'''Understanding __init__ Constructor'''

class Company:
    company = "GOOGLE\n"
    location = "Banglore"
    
    def __init__(self):
        print("")
        print("Company is created!!")

    def empDetails(self, signature):
        print("")
        print(f"Employee Name: {self.name} and his Salary is {self.salary}. He is current Location is {self.location}. {signature}")
        
    @staticmethod #No need for self after this.
    def greetings():
        print("Great!!!!!!\n")

emp = Company() #Object Instantiation
print(Company.company)
num_emp = int(input("Enter no. of employees in the company: "))
for i in range(num_emp):
    emp.name = input("Enter your name: ")
    emp.salary = int(input("Enter your salary: "))
    emp.empDetails("<Google>") # Company.empDetails(emp, "<Google>")
    emp.greetings() # Company.greetings()
    