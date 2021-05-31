# Function for sum of first N natural numbers. 

def sum_n(n):
    sum = 0
    for i in range(n+1):
        sum = sum+i
    return sum

def sum_n_recur(n):
    sum = 0
    if n==0:
        return 0
    else:
        sum = n + sum_n_recur(n-1)
    return sum

num = int(input("Enter the number till which u want sum\n"))
print("Sum is: ", sum_n(num))
print("Sum is: ", sum_n_recur(num))