# PATTERN PRINTING

try:
    n = int(input("Enter the number of rows u want: "))
    print("Option1: Simple Right angled triangle. Enter any +integer")
    print("Option2: Upsidedown Right angled triangle. Enter 0")
    opt = bool(int(input("Enter your option ")))
    print(opt)
    if opt:
        for i in range(1,n+1):
            print("*"*i, end="")
            print("")
    else:
        for i in range(n,0,-1):
            print("*"*i, end="")
            print("")
except Exception as e:
    print("Make sure you enter a number!")