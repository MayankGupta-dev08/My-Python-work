'''Class method as an alternative constructor'''
# We use this were we need to get the attributes for different objects from a given pattern of a string ana it could be from a file where there are many such strings. So we could use this to make our work easy.

class Employee:
    no_of_leaves = 15

    def __init__(self, aname, asal, arole):
        self.name = aname
        self.salary = asal
        self.role = arole

    def printDetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves # this will change the class attribute no_of_leaves.

    @classmethod
    def Alter_constr(cls, str):
        lst_param = str.split("-") # str.split() will create a list after spliting using '-' 
        # print(lst_param)
        # print(type(lst_param))
        return cls(lst_param[0], lst_param[1], lst_param[2])

    # Shortcut of the above Alter_constr(cls, str) could be done a bit differently using *args. 
    '''Better Method'''
    # @classmethod
    # def Alter_constr(cls, str):
    #     return cls(*str.split("-"))  
    # By this we don't need those 3 lines also.


harry = Employee("harry", 52663, "student")
rohan = Employee("rohan", 54633, "student")
karan = Employee.Alter_constr("karan-97633-Instructor")
# the above line will firstly call Alter_constr() and it will split str and store in form of a list and return it to class (__init__) with all parameters to be stored for this object just like for the other two.

print(harry.no_of_leaves)
rohan.change_leaves(16)
print(karan.name)
print(karan.no_of_leaves)
print(harry.no_of_leaves)
print(karan.printDetails())
print(rohan.printDetails())