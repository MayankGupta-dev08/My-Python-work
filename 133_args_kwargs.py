'''n Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:
args and kwargs.

1.)*args (Non-Keyword Arguments)
We can use any word in place of arg, but it should contain '*' before its nanme  - *name.

What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined.

With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).

For example : we want to make a multiply function that takes any number of arguments and able to multiply them all together. It can be done using *args.

Using the *, the variable that we associate with the * becomes an iterable meaning you can do things like iterate over it, run some higher-order functions such as map and filter, etc

2.)**kwargs (Keyword Arguments)
The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).

A keyword argument is where you provide a name to the variable as you pass it into the function.

One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.

'''

# 1.    Python program to illustrate *args for variable number of arguments
def myFun(*argv):
	for i in argv:
		print (i)
print("1.    Python program to illustrate *args for variable number of arguments")
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# 2.    Python program to illustrate *args with first extra argument
# def myFun(*argv, arg1): We cant write like this normal agument if present in funtion then its always comes before *args and **kwargs.

def myFun(arg1, *argv):
	print ("First argument :", arg1)
	for arg in argv:
		print("Next argument through *argv :", arg)
print("")
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# 3.    Python program to illustrate *kargs for variable number of keyword arguments
def myFun(**kwargs):
	for key, value in kwargs.items():
		print ("%s == %s" %(key, value))
# Driver code
print("")
myFun(first ='Geeks', mid ='for', last='Geeks')


# 4.    Python program to illustrate **kargs for variable number of keyword arguments with one extra argument.

def myFun(arg1, **kwargs):
    
    print("arg1", arg1)
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))

# Driver code
print("")
myFun("Hi", first ='Geeks', mid ='for', last='Geeks')


# 5.    Python program to illustrate use of both *args and **kargs.
def myFun(arg1, arg2, arg3):
	print("arg1:", arg1)
	print("arg2:", arg2)
	print("arg3:", arg3)
	
# Now we can use *args or **kwargs to pass arguments to this function :
args = ("Geeks", "for", "Geeks")
print("")
myFun(*args)

kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"}
myFun(**kwargs)


# 6.    Python program to illustrate use of both *args and **kargs, in same line to call a function.
def myFun(*args,**kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)

# Now we can use both *args ,**kwargs to pass arguments to this function :
print("")
myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")



# From Code with Harry

# def func(a, b, c, d, e):
#     print(a, b, c, d, e)

def func1(normal, *arg1, **kwargs1):
    print(normal)
    for item in arg1:
        print(item)
    print("Now we would like to introduce **kwargs")
    for k,v in kwargs1.items():
        print(f"{k} -=> {v}")
print("")
func1(34, "I am", "a good", "boy", first="ABC", second="PQS", third="XYZ")