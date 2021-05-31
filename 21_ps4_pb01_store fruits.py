# write a programme to store seven fruits in a list, entered by the user.

# Method 1
'''f1 = input("Enter your Fruit number 1: ")
f2 = input("Enter your Fruit number 2: ")
f3 = input("Enter your Fruit number 3: ")
f4 = input("Enter your Fruit number 4: ")
f5 = input("Enter your Fruit number 5: ")
f6 = input("Enter your Fruit number 6: ")
f7 = input("Enter your Fruit number 7: ") 

FruitList = [f1, f2, f3, f4, f5, f6, f7]
print(FruitList) '''

# Method 2
FruitList = []
for i in range(7):
    f1 = input("Enter your Fruit number " + str(i+1) + ": ")
    FruitList.append(f1)
    print(FruitList)
print("Final Friuts list: ", FruitList)