'''try, except, finally'''
# finally will run regardless of error.

try:
    a = int(input("Enter a number to be divided by 1: "))
    b = 1/a
    print(b)

except ValueError as e:
    print(e)
    exit()
finally:
    print("We are done!!")
# If we haven't written finally then due to exit, the above print line would not get executed but now it will.

print("Thanks for using the code") # This will only print after successful termination of try.