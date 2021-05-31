'''try with else'''
# else will only run after successful completion of try.

try:
    a = int(input("Enter a number to be divided by 1: "))
    b = 1/a
    print(b)

except ValueError as e:
    print(e)
else:
    print("We were successful!!")
    print("Thanks for using the code")