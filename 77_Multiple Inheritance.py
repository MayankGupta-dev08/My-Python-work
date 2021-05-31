'''Example of Multiple Inheritance'''

class Employee:
    company = "MICROSOFT"
    eCode = 133
    def showDetails(self):
        print(f"This is an Employee of {self.company}\n")

class FreeLancer:
    company = "FIVERR"
    level = 1
    def showDetails(self):
        print(f"This is an Freelancer of {self.company}\n")
    def upgardeLevel(self):
        self.level +=1    

class Programmer(FreeLancer, Employee):
    name  = "Mannu"
    language = "Python"
    def getLanguage(self):
        print(f"The lanuage is {self.language}")

    def showDetails(self):
        print(f"Hi, I am {self.name} and I am a Programmer, having proficiency in {self.language}.\n")

p = Programmer()
p.showDetails()
print(p.company)
Employee.showDetails(p)
FreeLancer.showDetails(p)
e=Employee()
e.showDetails()