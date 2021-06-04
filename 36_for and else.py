'''Use of else along with fro loop'''

# 1. Example 1
for i in range(10):
    print(i, end=" ")
else:
    print("For loop ended properly!!\n") #Here it will print this line after the loop.


# 2. Example 2
# this will give you clear idea about this for-else
print("Example for Break keyword and also for-else statement")
for i in range(10):
    print(i, end=" ")
    if(i==5):
        break
else:
    print("This will not be printed as for loop is interruped by break statement.") # Here it will not print this line after the loop as the loop is not successfully terminated rather it is forcefully terminated or interrupted by break statement.

# 3. Example 3
khana = ["roti", "sabzi", "daal", "chawal", "lassi", "salad", "dessert"]
print("")
check = input("Enter the name of item you want to check\n")
for dish in khana:
    if check == dish:
        break
else:
    print("Your item is not in khana")


# 4. Use of continue statement in for loops
print("\nExample for Continue keyword")
for i in range(10):
    if(i==5):
        continue
    print(i, end=" ")