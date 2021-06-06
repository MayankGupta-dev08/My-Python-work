'''try, except, finally'''
# finally will run regardless of error.

try:
    a = int(input("Enter a number to be divided by 1: "))
    b = 1/a
    print(b)

except ValueError as e:
    print(e)
    exit()

else:
    print("This will only be shown if try has been run sucessfully.")

finally:
    print("We are done!!")
# As the name suggests that this will be done finally and it will get executed regardless of execution of try and except. 
# It is generally used to code clean up, closed open files, endnote etc.
# If we haven't written finally then due to exit, the above print line would not get executed but now it will.

print("Thanks for using the code") # This will only print after successful termination of try, i.e. only if except has not run.