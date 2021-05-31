'''Example of Multilevel Inheritance'''

class Company:
    company_name = "TATA & SONS"
    location = "India"
    def showDetails(self):
        print(f"This is {self.company_name} Company.")

class Subsidiary(Company):
    company_name = "TCS"
    work = "Consultancy"
    def showDetails(self):
        print(f"This is {self.company_name} Subsidiary Company and its work is {self.work}.")

class Programmer(Subsidiary):
    name  = "Mannu"
    language = "Python"
    def showDetails(self):
        print(f"Hi, I am {self.name} and I am a Programmer, having proficiency in {self.language}.")

p = Programmer()
p.showDetails()
print(p.company_name)
print(p.location)
print(p.work)
s=Subsidiary()
s.showDetails() # Subsidiary.showDetails(p) #--> works same.
c=Company()
c.showDetails() # Company.showDetails(p) #--> works same.