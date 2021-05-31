'''Understanding self'''

class Employee:
    company = "Google"
    location = "Banglore"

    def __init__(self, aname, sal):
        self.name = aname
        self.salary = sal
        
    def empDetails(self):
        print(f"Employee Name: {self.name} and the company which he works in is {self.company} and his salary is {self.salary}. He is currently in {self.location}.")

# mridul.name = "Mridul Gupta"
# mridul.salary = 50000000
# mayank.name = "Mayank Gupta"
# mayank.salary = 10000000

mridul = Employee("Mridul Gupta", 50000000) #Object Instantiation when we have a constructor.
mayank = Employee("Mayank Gupta", 10000000) #Object Instantiation when we have a constructor.

mayank.company = "Amazon" # Here, we are creating an attribute/property only for instance mayank, if its already in class than it will overwrite but just fro mayank.

mridul.empDetails() #Usual way of calling the member function.
print(mridul.__dict__, "\n")
Employee.location = "Delhi"
# Here we have changed the class attribute from prev one.
mayank.empDetails()
print(mayank.__dict__, "\n")
mridul.empDetails()
print(mridul.__dict__)

# Employee.empDetails(mayank) 
# # Rare way of calling a member function using an object of that class.