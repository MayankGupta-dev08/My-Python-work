# programme for asking the elements of a Dictionary from user.

userDict = {}
n = int(input("Enter the number of elements (Key-Value pair) you wish to enter in your Dictionary: "))
for i in range(n):
    k = input("Enter your "+str(i+1)+" Key: ")
    v = input("Enter your "+str(i+1)+" Value: ")
    userDict.update({k:v})

print("\n" , userDict)
print(type(userDict))