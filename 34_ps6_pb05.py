# Write a program to check whether a name exist in a list or not. 

nameL = ["mannu", "puru", "pulkit", "ashu", "kake", "anuj", "mohit", "ankit", "divya", "sumit"]
name = input("Enter the name: ")
name = name.lower()

if name in nameL:
    print("Yes, it's present.")
else:
    print("No, it's not present.")