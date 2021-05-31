# Factorial program using user defined function and user defined recursion function.

fact = 1
def factorial_iter(n):
    for i in range(n):
        fact = fact*(i+1)
    return fact

def factorial_recur(m):
    if m == 1 or m == 0:
        return 1
    else:
        return m*factorial_recur(m-1)

num = int(input("Enter number to find Factorial of: "))
print(factorial_iter(num))
print(factorial_recur(num))
