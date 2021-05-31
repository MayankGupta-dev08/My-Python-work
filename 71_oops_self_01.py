'''Understanding self'''

class Employee:
    company = "Google"
    location = "Banglore"
    def empDetails(self):
        print(f"Employee Name: {self.name} and the company which he works in is {self.company} and his salary is {self.salary}. He is currently in {self.location}.\n")

mridul = Employee() #Object Instantiation
mridul.name = "Mridul Gupta"
mridul.salary = 50000000

mayank = Employee() #Object Instantiation
mayank.name = "Mayank Gupta"
mayank.salary = 10000000
mayank.company = "Amazon"

print("")
mridul.empDetails() #Usual way of calling the member function.
Employee.empDetails(mayank) #Rare way of calling the member function, but this will show u why, self as an instance is impotant, beacuse both line 10 and 11 are exactly same, so that's why self is must in member functions alongside anyother argument (if any required).

