''' Understanding the conccept of Overriding in classes and the use  of super()'''

'''Example1'''
class A:    # class A with classvar1 and __init__ 
    classvar1 = "class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
    

class B(A): # class B extending class A with classvar2 
    classvar2 = "class variable in class B"


a = A()  # runs the constructor of class A
b = B()  # Since it doesn't have it's own constructor so, runs the constructor of class A and lets this instance know that their is one var1 also.
print(b.classvar2)  # class variable in class B
print(b.classvar1)  # class variable in class A    
print(b.var1, "\n") # I am inside class A's Constructor   


'''Example2'''
class A: # class A with classvar1 and __init__
    classvar1 = "class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
        self.classvar1 = "Instance variable in class A"
    

class B(A): # class B extending class A with classvar2 
    classvar2 = "class variable in class B"


a = A()  # runs the constructor of class A
b = B()  # Since it doesn't have it's own constructor so, runs the constructor of class A and gets var1 and classvar1 for that instance.
print(b.classvar2)  # OUTPUT - class variable in class B
print(b.classvar1, "\n")  # OUTPUT - Instance variable in class A

# NOTE - Although both were present, class variable and instance variable but it will firstly choose an instance variable as it's pointing to that instance which is created by constructor and not class variable, if it was not there than it had gone to class A and asked if it was class variable then take it.


'''Example3 - Overriding the attribute'''
class A: # class A with classvar1 and __init__
    classvar1 = "class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
        self.classvar1 = "Instance variable in class A"
            

class B(A): # class B extending class A
    classvar1 = "class variable in class B"


a = A()  # runs the constructor of class A
b = B()  # Since it doesn't have it's own constructor so, runs the constructor of class A and gets var1
print(b.classvar1, "\n")  # OUTPUT - class variable in class B.
# As it has its own classvar1 so it will override the value got from class A's constructor


'''Example4 - Overriding the constructor and the attribute'''
class A: # class A with classvar1 and __init__
    classvar1 = "class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
        self.classvar1 = "Instance variable in class A"
            

class B(A): # class B extending class A with __init__
    classvar1 = "class variable in class B"

    def __init__(self):
        self.var1 = "I am inside class B's Constructor"
        self.classvar1 = "Instance variable in class B"

a = A()  # runs the constructor of class A
b = B()  # runs the constructor of class B,
print(b.var1)             # OUTPUT - I am inside class B's Constructor
print(b.classvar1, "\n")  # OUTPUT - Instance variable in class B
# As it has its own constructor so it will not run class A's constructor, unless super is used.
# As it has its own classvar1 and also the constructor is changing the value of classvar1 so it will override and consider the instance value given by constructor of class B.


'''Example5'''
class A: # class A with classvar1 and __init__
    classvar1 = "class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
        self.classvar1 = "Instance variable in class A"
        self.var2 = "Special"    

class B(A): # class B extending class A with __init__
    classvar1 = "class variable in class B"

    def __init__(self):
        super().__init__()  # Calling the constructor of super class
        self.var1 = "I am inside class B's Constructor"
        self.classvar1 = "Instance variable in class B"
        print(super().classvar1)

a = A()  # runs the constructor of class A
b = B()  # runs the constructor of class B,
# Line 102              # OUTPUT - Instance variable in class A
print(b.var1)           # OUTPUT - I am inside class B's Constructor
print(b.classvar1)      # OUTPUT - Instance variable in class B
print(b.var2, "\n")     # OUTPUT - Special
# NOTE - If super().__init__() was not written then print(b.var2, "\n") would have given error, as both the instances ie. of a and b are different and var2 is instance variable not class variable, with class B also having its constructor, var2 is not directly accessible to class B object b so to do this we have to use super to call class A constructor for object b. 


'''Example6'''
class A: # class A with classvar1 and __init__
    classvar1 = "class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
        self.classvar1 = "Instance variable in class A"
        self.var2 = "Special"    

class B(A): # class B extending class A with __init__
    classvar1 = "class variable in class B"

    def __init__(self):
        self.var1 = "I am inside class B's Constructor"
        self.classvar1 = "Instance variable in class B"
        super().__init__()  # Calling the constructor of super class and changing value of var1 and classvar1 for this instance..

a = A()  # runs the constructor of class A
b = B()  # runs the constructor of class B,
print(b.var1)           # OUTPUT - I am inside class A's Constructor
print(b.classvar1)      # OUTPUT - Instance variable in class A
print(b.var2, "\n")     # OUTPUT - Special

# NOTE - If super().__init__() was not written then print(b.var2, "\n") would have given error, as both the instances ie. of a and b are different and var2 is instance variable not class variable, with class B also having its constructor, var2 is not directly accessible to class B object b so to do this we have to use super to call class A constructor for object b. 

