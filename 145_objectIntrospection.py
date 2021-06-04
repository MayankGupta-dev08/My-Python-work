'''OBJECT INTROSPECTION'''

class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def name(self):
        return f"The name is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None and self.lname == None:
            return f"No email exist!!, Please set!"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, c_email):
        print("Email changed to: ", c_email)
        print("Setting others now.....")
        nameLst = c_email.split("@")[0]
        self.fname = nameLst.split(".")[0]
        self.lname = nameLst.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillF = Employee("Skill", "F")
print(skillF.name())
print(skillF.email)
print(type(skillF))
print(id(skillF))
print(dir(skillF))
print("")
print("This is a string")
print(type("This is a string"))
print(id("This is a string"))
print(dir("This is a string"), "\n\n")

import inspect
class Employee2:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

def insp(emp):
     inspect.isclass(emp)
     while True:
       print(dir(emp))
       break

Shivansh=Employee2("Shivansh","Varshney")
emp=input()
insp(emp)