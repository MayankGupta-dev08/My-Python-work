try:
    a = int(input("Enter a number to be divided by 1: "))
    b = 1/a
    print(b)

except ValueError as e:
    print("Make sure u are entering a number")
except ZeroDivisionError as e:
    print("Make sure u are not entering a 0")
except TypeError as e:
    print("This is a type error")

print("Thanks for using the code")