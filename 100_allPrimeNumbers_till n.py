'''PRINT ALL PRIME NUMBERS TILL N'''

n = int(input("Enter the number till which u want prime numbers: "))
if n<=1:
    print("Not Prime")
else:
    for i in range(2,n+1):
        count = 0
        for j in range(2,i):
            if i%j==0:
                count +=1
                break
        if count==0:
            print(i, end=" ")
            
# To check from 1 to 100
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.