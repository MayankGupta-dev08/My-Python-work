# sum of first n natural number

num = int(input("Enter the number till which u want sum: "))
i =1
sum = 0
while i<=num:
    sum  = sum + i
    print(i)
    i = i+1

print("Sum of first n natural no.s: ", sum)
print("Average of first n natural no.s: ",sum/num)