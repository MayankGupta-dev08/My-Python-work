#the faulty calculator
"""
design a calculator which will correctly solve all the problems except the following ones:
45*3=555, 56+9=77, 56/6=4
your program take two operator and the two numbers qs input from the user and the return the result
"""

d = {"45*3":555, "56+9":77, "56/6":4}
while(1):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter the operator: ")
    a_ = str(a) + op + str(b)
    b_ = str(b) + op + str(a)
    if a_ in d:
        print(d[a_])
        break
    elif b_ in d:
        print(d[b_])
        break
    elif op=='+' or op=='*' or op=='-' or op=='/':
        if op=='+':
            print("your ans is : ", a+b)
        elif op=='-':
            print("your ans is : ", a-b)
        elif op=='*':
            print("your ans is : ", a*b)
        else:
            print("your ans is : ", a/b)
        break
    else:
        print("Again enter values")