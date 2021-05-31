class Employee:
    #Class Attributes
    company = "Google"
    salary = "5000k USD" #these can be of any data type
    location = "Banglore"

mridul = Employee() #Object Instantiation
mayank = Employee() #Object Instantiation

mayank.name = "Mayank Gupta" #adding Instance Attribute
mridul.name = "Mridul Gupta" #adding Instance Attribute
mridul.salary = "5500k USD" #adding Instance Attribute, this will be given priority over class attribute salary during assignment and retrieval.

print("")
print(f"Employee: {mayank.name}, Company:{mayank.company}, Location:{mayank.location}, Salary:{mayank.salary}") 
print(f"Employee: {mridul.name}, Company:{mridul.company}, Location:{mridul.location}, Salary:{mridul.salary}\n") #Here, u can see that Instance attribute (salary = 5500k) is given prefernce over 5000k.

Employee.location = "Silicon Valley" #Changing the Class Attribute permanantly.
print("After location change....\n")
print(f"Employee: {mayank.name}, Company:{mayank.company}, Location:{mayank.location}, Salary:{mayank.salary}") 
print(f"Employee: {mridul.name}, Company:{mridul.company}, Location:{mridul.location}, Salary:{mridul.salary}")

# print(mayank.age)
# This above libe will throw an error as age is not present as instance or class attribute. 
