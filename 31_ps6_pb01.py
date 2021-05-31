# Write a programme to print greatest of four numbers entered by the user.

# METHOD 1
# num1 = int(input("Enter your 1st number: "))
# num2 = int(input("Enter your 2nd number: "))
# num3 = int(input("Enter your 3rd number: "))
# num4 = int(input("Enter your 4th number: "))

# if (num1>=num2 and num1>=num3 and num1>=num4):
#     print("Greatest of four numbers is: ", num1)
# elif (num2>=num1 and num2>=num3 and num2>=num4):
#     print("Greatest of four numbers is: ", num2)
# elif (num3>=num1 and num3>=num2 and num3>=num4):
#     print("Greatest of four numbers is: ", num3)
# else:    
#     print("Greatest of four numbers is: ", num4)

# METHOD 2
# if (num1>=num2):
#     g1 = num1
# else:
#     g1 = num1
# if (num3>=num4):
#     g2 = num3
# else:
#     g2 = num4

# if (g1>=g2):
#     print("Greatest of four numbers is: ", g1)
# else:    
#     print("Greatest of four numbers is: ", g2)


# METHOD 3
m = -10e9
n = int(input("How many numbers do u want to compare: "))
for i in range(n):
    temp = int(input("Enter " +str(i+1)+ " number: "))
    m = max(m, temp)

print("Greatest of four numbers is: ", m)

