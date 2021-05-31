'''
for n = 3
  *
 ***
*****
 ***
  *
'''


n = int(input("Enter the number of levels for the pattern: "))

spaces = n-1
star = 1
for i in range(n):
    print(" "*spaces, end="")
    print("*"*star, end="")
    print(" "*spaces)
    star +=2
    spaces -=1

# Since, at the end of loop, star is getting increased by 2 and spaces is decreased by 1 additionaly than required, so we have to do the below thing.
star -=4
spaces +=2
 
for j in range(n-1):
    print(" "*spaces, end="")
    print("*"*star, end="")
    print(" "*spaces)
    star -=2
    spaces +=1
    