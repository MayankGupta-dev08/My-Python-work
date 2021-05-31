# To find greatest of three numbers by defining function. 

def greatest(n1,n2,n3):
    g = n1
    if n1>n2:
        if n1>n3:
            g=n1
        else:
            g=n3
    else:
        if n2>n3:
            g=n2
        else:
            g=n3
    return g

num1 = int(input("Enter your 1st number: "))
num2 = int(input("Enter your 2nd number: "))
num3 = int(input("Enter your 3rd number: "))
result = greatest(num1, num2, num3)
print("\nMaximum of the three: ", result)