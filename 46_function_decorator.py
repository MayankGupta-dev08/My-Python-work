'''Without function decorator'''

def dec1(func1):
    def nowexec():
        print("Executing now...")
        func1()
        print("Executed!\n")
    return nowexec

def whoIsMayank():
    print("Mayank is a good boy.")

whoIsMayank = dec1(whoIsMayank)
whoIsMayank()

'''With function decorator'''

def dec1(func1):
    def nowexec():
        print("Executing now...")
        func1()
        print("Executed!")
    return nowexec

@dec1
def whoIsMayank():
    print("Mayank is a good boy.")

# whoIsMayank = dec1(whoIsMayank)
whoIsMayank()

'''Output is same for both the cases'''
# Executing now...
# Mayank is a good boy.
# Executed!


'''Explanation'''
# 	1. Here, firstly dec1 will be called and it has whoIsMayank as func1(). 
# 	2. Inside dec1, nowexec() is defined only but now it will not be executed.
# 	3. Dec1 will simply return nowexec to whoIsMayank  (function copying).
# 	4. Now, when whoIsMayank called it will actually call nowexec() and it only will run.
# 	5. Printing 1st line as - Executing now...
# 	6. Calling func1 which is actually original whoIsMayank, as it was pointing to it.
# 	7. Printing 2nd line as - Mayank is a good boy.
# 	8. Printing 3rd line as - Executed!
#   9. End


'''Syntax: @nameOfFunction
Use of this decorator :-'''
# 	1. When we want to use many different functions as an argument of a Function and keep on using that Function many times.
# Eg - Here, like whoIsMayank there can be few more functions which could be used after placing a decorator (@dec1).