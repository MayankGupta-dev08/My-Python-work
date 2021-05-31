'''Example of super() in Multilevel Inheritance'''

class Company:
    company_name = "TATA & SONS"
    location = "India"
    def showDetails(self):
        print(f"This is {self.company_name} Company.")

class Subsidiary(Company):
    company_name = "TCS"
    work = "Consultancy"
    def showDetails(self):
        super().showDetails()
        print(f"This is {self.company_name} Subsidiary Company and its work is {self.work}.")

class Programmer(Subsidiary):
    name  = "Mannu"
    language = "Python"
    def showDetails(self):
        super().showDetails()
        print(f"Hi, I am {self.name} and I am a Programmer, having proficiency in {self.language}.")

p = Programmer()
print(p.company_name)
print(p.location)
print(p.work)
Company.showDetails(p)
Subsidiary.showDetails(p) 
p.showDetails()


'''OUTPUT'''
# TCS
# India
# Consultancy
# This is TCS Company.
# This is TCS Company.
# This is TCS Subsidiary Company and its work is Consultancy.   
# This is TCS Company.
# This is TCS Subsidiary Company and its work is Consultancy.   
# Hi, I am Mannu and I am a Programmer, having proficiency in Python.
