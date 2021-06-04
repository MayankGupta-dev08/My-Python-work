'''OBJECT INTROSPECTION using inspect module
The inspect module helps in checking the objects present in the code that we have written. As Python is an OOP language and all the code that is written is basically an interaction between these objects, hence the inspect module becomes very useful in inspecting certain modules or certain objects. We can also use it to get a detailed analysis of certain function calls or tracebacks so that debugging can be easier.
'''

'''Methods to verify the type of token:'''

# 1.  isclass(): The isclass() method returns True if that object is a class or false otherwise. When it is combined with the getmembers() functions it shows the class and its type. It is used to inspect live classes.
import inspect # import required modules

class A(object): # create class
	pass

# use isclass()
print(inspect.isclass(A))


# 2.    ismodule(): This returns true if the given argument is an imported module.
import inspect # import required modules
import time

# use ismodule()
print(inspect.ismodule(time))


# 3.  ismethod(): This method is used to check if the argument passed is the name of a method or not.
import inspect # import required modules
import collections

# use ismethod()
print(inspect.ismethod(collections.Counter))


# 4.  isfunction(): This method returns true if the given argument is an inbuilt function name.
import inspect # import required modules

# explicit function
def fun(a):
	return 2*a

# use isfunction()
print(inspect.isfunction(fun), "\n")


'''Methods to retrieve the source of token:'''

# 1.  getclasstree(): The getclasstree() method will help in getting and inspecting class hierarchy. It returns a tuple of that class and that of its preceding base classes. That combined with the getmro() method which returns the base classes helps in understanding the class hierarchy.

# import required module
import inspect

# create classes
class A(object):
	pass

class B(A):
	pass

class C(B):
	pass

# not nested
print(inspect.getmro(C))
print("")
# nested list of tuples
for i in (inspect.getclasstree(inspect.getmro(C))):
    print(i, "\n")
print("")


# 2.  getmembers(): This method returns the member functions present in the module passed as an argument of this method.
# import required module
import inspect
import math

# shows the member functions of any module or object
print(inspect.getmembers(math),"\n")


# 3.  signature(): The signature() method helps the user in understanding the attributes which are to be passed on to a function.
# import required modules
import inspect
import collections

# use signature()
print(inspect.signature(collections.Counter),"\n")


# 4.  stack(): This method helps in examining the interpreter stack or the order in which functions were called.
# import required module
import inspect

# define explicit function
def Fibonacci(n):
	if n < 0:
		return 0

	elif n == 0:
		return 0

	elif n == 1:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)


# Driver Program
(Fibonacci(12))

# inpsecting interpreter stack
print(inspect.stack(),"\n")


# 5.  getsource(): This method returns the source code of a module, class, method, or a function passes as an argument of getsource() method.
# import required modules
import inspect

def fun(a,b):
	# product of
	# two numbers
	return a*b

# use getsource()
print(inspect.getsource(fun))

