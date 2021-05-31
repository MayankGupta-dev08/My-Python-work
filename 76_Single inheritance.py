'''Example of Single Inheritance'''

class Employee:
    company = "GOOGLE"

    def showDetails(self):
        print("This is an Employee\n")

class Programmer(Employee):
    language = "Python"
    company = "YOUTUBE" #After this class programmer will not use the above comapny name which was of its base class.

    def getLanguage(self):
        print(f"The lanuage is {self.language}")

    def showDetails(self):
        print("This is a Programmer\n")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(e.company)
print(p.company)