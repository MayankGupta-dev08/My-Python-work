'''
n = 5

 1 1 1 1 1     i->0 
 1       1
 1       1
 1       1
 1 1 1 1 1     i = 4

j = 0    j = n-1

'''

n = int(input("Enter the number of levels: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print("")