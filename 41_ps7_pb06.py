# Factorial of a given number

num = int(input("Enter the number for factorial: "))
fact = 1

for i in range(1,num+1):
    fact = fact*i
print("Factorial of the given number: ",fact)