# Write a program to ask 8 numbers from the user and print all the unique numbers at once.

print("You have to enter 8 numbers of your choice\n")
set1 = set()
for i in range(8):
    n = int(input("Enter number"+str(i+1)+" : "))
    set1.add(n)
print("List of your chosen unique numbers is: ", set1)

# Easy but Lengthy method
# num1 = int(input("Enter number1: \n"))
# num2 = int(input("Enter number2: \n"))
# num3 = int(input("Enter number3: \n"))
# num4 = int(input("Enter number4: \n"))
# num5 = int(input("Enter number5: \n"))
# num6 = int(input("Enter number6: \n"))
# num7 = int(input("Enter number7: \n"))
# num8 = int(input("Enter number8: \n"))

# s1 = {num1, num2, num3, num4, num5, num6, num7, num8}
# print(s1)
