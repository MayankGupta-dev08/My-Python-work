'''printing following pattern

****
***         n=4
**
*

'''
def pattern(n):
    print("")
    for i in range(n):
        print("*"*(n-i), end="")
        print(" "*i)

num = int(input("Enter the number of lines: "))
pattern(num)