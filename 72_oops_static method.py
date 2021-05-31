'''USE OF @staticmethod'''

class Company:
    company = "GOOGLE\n"
    location = "Banglore"
    
    def empDetails(self, signature):
        print("")
        print(f"Employee Name: {self.name} and his Salary is {self.salary}. He is current Location is {self.location}. {signature}")
        
    @staticmethod #No need for self after this.
    def greetings():
        print("Great!!!!!!\n")

emp = Company() #Object Instantiation
print("")
print(Company.company)
num_emp = int(input("Enter no. of employees in the company: "))
for i in range(num_emp):
    emp.name = input("Enter your name: ")
    emp.salary = int(input("Enter your salary: "))
    emp.empDetails("<Google>") #This <Google> will pass as an argument to empDetails other than self, i.e. signature.
    # Line 19 could also be written as --> Company.empDetails(emp, "<Google>")
    emp.greetings() # Company.greetings()
    