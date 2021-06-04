'''Use of @property, @at_name.setter, @at_name.deleter'''

# NOTE - Best way to change an attribute/property and if we want to change any other attribute using that property than we have to use setter.

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

hindustani_bhau = Employee("Hindustani", "bhau")

print(hindustani_bhau.name())
print(hindustani_bhau.email, "\n")
hindustani_bhau.fname = "Indian"
print(hindustani_bhau.name())
print(hindustani_bhau.email, "\n")

hindustani_bhau.email = "Hindu.bhai@gmail.com"
print(hindustani_bhau.fname)
print(hindustani_bhau.lname)
print(hindustani_bhau.name(), "\n")

# del hindustani_bhau.fname     # This will delete normal attribute easily.
# print(hindustani_bhau.fname)  # This will give error, as it's already deleted by above line.

# NOTE - But if we will try to do same with email which is made using property decorator then we have to use create another function using another decorator.
del hindustani_bhau.email
print(hindustani_bhau.email)

'''OUTPUT'''
# The name is Hindustani bhau
# Hindustani.bhau@gmail.com

# The name is Indian bhau
# Indian.bhau@gmail.com

# Email changed to:  Hindu.bhai@gmail.com
# Setting others now.....
# Hindu
# bhai
# The name is Hindu bhai