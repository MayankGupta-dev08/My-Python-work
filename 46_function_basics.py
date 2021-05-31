'''We can create a copy of a function and we can also delete a function.'''
# Its very obvious that we can have nested functions (functions in a Function).

def func1():
    print("this is a function!\n")

func2 = func1 # Creating a copy of a func1 function.
# Its different from func2 = func1(), as in this func2 will get what is returned by func1.

del func1
# deleting a function

func2()
# calling func2


'''We can return a function through another function.'''

def func3(num):
    if num==0:
        return print # print is an inbuilt function
    elif num==1:
        return sum # sum is also an inbuilt function
    else:
        return input # input is also an inbuilt function

n = int(input("Enter either 0 or 1: "))
result = func3(n)
print(result, "\n")


'''We can pass a function as an argument/parameter in another function.'''

def func4(p1):
    p1("We can pass a function as an argument/parameter in another function.")

func4(print)
print("Above line was printed using func4 by passing print as an argument and then using it as a function.\n")