'''Format method in strings
before the use of fstring, format was used, but in some languages it's still used.'''

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
# name = f"The name is {fname} {lname}."
name = "Your name is {} {}.".format(fname, lname)
print(name)
name = "Your name is {1} {0} and he is {2}.".format(fname, lname, "cool")
print(name)