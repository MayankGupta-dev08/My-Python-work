'''Explanation of PROPERTY DECORATOR through examples'''

class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@gmail.com"

    def name(self):
        return f"The name is {self.fname} {self.lname}"

    # def email(self):
    #     return f"{self.fname}.{self.lname}@gmail.com"

hindustani_bhau = Employee("Hindustani", "bhau")
nikhil_raj = Employee("Nikhil", "raj")

print(hindustani_bhau.name())
print(hindustani_bhau.email, "\n")
hindustani_bhau.fname = "Indian"
# NOTE - Once the object hindustani_bhau is created and fname and lname are already passed as arguments and email is created using that in constructor then after changing fname from the above line only fname will change but email will remain same as it was created by constructor at first run time and not recomputed.
print(hindustani_bhau.name())
print(hindustani_bhau.email, "\n\n")

'''OUTPUT'''
# The name is Hindustani bhau
# Hindustani.bhau@gmail.com 

# The name is Indian bhau
# Hindustani.bhau@gmail.com


class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def name(self):
        return f"The name is {self.fname} {self.lname}"

    def email_add(self):
        self.email = f"{self.fname}.{self.lname}@gmail.com"
        return self.email

hindustani_bhau = Employee("Hindustani", "bhau")
nikhil_raj = Employee("Nikhil", "raj")

print(hindustani_bhau.name())
print(hindustani_bhau.email_add(), "\n")
hindustani_bhau.fname = "Indian"
# NOTE - Now, email will be changed along with fname as it is recomputed when function is called again.
print(hindustani_bhau.name())
print(hindustani_bhau.email) # Here it's still not changed as we have changed fname but email_add() is still not called so email is not changed and still previous one.
print(hindustani_bhau.email_add())
print(hindustani_bhau.email, "\n\n") # Here, it changed one, as emil_add() is already called.

'''OUTPUT'''
# The name is Hindustani bhau
# Hindustani.bhau@gmail.com 

# The name is Indian bhau   
# Hindustani.bhau@gmail.com

# The name is Hindustani bhau
# Hindustani.bhau@gmail.com

# The name is Indian bhau
# Hindustani.bhau@gmail.com
# Indian.bhau@gmail.com
# Indian.bhau@gmail.com


# NOTE - Best way to change an attribute/property.
class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def name(self):
        return f"The name is {self.fname} {self.lname}"

    @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"


hindustani_bhau = Employee("Hindustani", "bhau")
nikhil_raj = Employee("Nikhil", "raj")

print(hindustani_bhau.name())
print(hindustani_bhau.email, "\n")
hindustani_bhau.fname = "Indian"
print(hindustani_bhau.name())
print(hindustani_bhau.email)

'''OUTPUT'''
# The name is Hindustani bhau
# Hindustani.bhau@gmail.com 

# The name is Indian bhau   
# Indian.bhau@gmail.com