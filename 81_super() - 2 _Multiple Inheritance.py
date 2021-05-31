'''Example of super() in Multilevel Inheritance'''
# Generally, super is used to call the constructor of the base class. 


class Company:
    company_name = "TATA & SONS"
    location = "India"
    def __init__(self):
        print(f"This is {self.company_name} Company.")

class Subsidiary(Company):
    company_name = "TCS"
    work = "Consultancy"
    def __init__(self):
        super().__init__()
        print(f"This is {self.company_name} Subsidiary Company and its work is {self.work}.")

class Programmer(Subsidiary):
    name  = "Mannu"
    language = "Python"
    def __init__(self):
        super().__init__()
        print(f"Hi, I am {self.name} and I am a Programmer, having proficiency in {self.language}.")

p = Programmer()


'''OUTPUT'''
# This is TCS Company.
# This is TCS Subsidiary Company and its work is Consultancy.   
# Hi, I am Mannu and I am a Programmer, having proficiency in Python.
