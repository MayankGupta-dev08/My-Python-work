'''
   *  n = 3                00 01 02 03 04
  ***                      10 11 12 13 14
 *****                     20 21 22 23 24 



    <- left | right -> 
 
'''

# j <= n-1
# 1 3 5 7 9 -> 1 -> 2*1+1 -> 2*3 +1

# n = int(input("Enter the number of lines for the pattern: "))
# left = n-2 # 1
# right = n # 3

# for i in range(n):
#     for j in range(2*(n-1)+1):
#         if j > left and j < right:
#             print("*", end="")
#         else:
#             print(" ",end="")
#     left -=1
#     right +=1
#     print("")

# 0 0 0 1 0 0 0 
# 0 0 1 1 1 0 0
# 0 1 1 1 1 1 0
# 1 1 1 1 1 1 1

n = int(input("Enter the number of levels: "))

spaces = n-1 #count
star = 1 #count

for i in range(n):
    print(" " * spaces, end = "")
    print("*" * star, end = "")
    print(" " * spaces)

    star += 2
    spaces -= 1     
