a = 84 #Global Variable
def func1():
    a=8 #Local Variable
    print(f"Printing Local variable: {a}")

func1()
print(f"Printing Global variable: {a}\n") 

b = 98 #Global Variable
def func2():
    global b # Now this function has access to global b, so any change to local b will change global b also.
    print(f"Printing Original Global variable: {b}")
    b = 4 #Changing the Global Variable
    print(f"Printing Local variable: {b}") 

func2()
print(f"Printing Changed Global variable: {b}") 