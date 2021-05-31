# Dictionary is a collection of key-value pair.

myDict = {
    "Mayank" : "Construction Manager",
    "Mridul" : "Coder",
    "Marks"  : [88, 86],
    "Dict2"  : {"Mannu":"Elder", "Puru":"Younger"},
    "H_No"   : 133,
    85642    : 1553
}

print(myDict) #printing dictionary
print(type(myDict), "\n")

print(myDict.keys()) #printing keys of dictionary
print(type(myDict.keys()), "\n")

print(list(myDict.keys()), "\n") #typecasting and printing of dictionary to list.

print(myDict.values()) #printing values of dictionary
print(type(myDict.values()), "\n")

print(myDict.items()) #prints the (key, value) for all contents of the dictionary.
print(type(myDict.items()), "\n")

# updating the dictionary
print(myDict, "\n")
newDict = {
    "Pulkit" : "Bro",
    "Divya" : "Sis",
    "Mridul" : "Bro"
}
myDict.update(newDict) #appends the dict by adding key-value pair from another dict at the end and also update the value of any key which is to be updated.
print(myDict)

print(myDict.get("Mayank")) #Prints value associated with the key "Mayank"
print(myDict["Mayank"]) #Prints value associated with the key "Mayank".

# This shows the difference between the .get() and [] syntax in dictionary. 
print(myDict.get("May@nk")) #Returns None as "May@nk" is not present in myDict as a key. 
print(myDict["May@nk"]) #Throws Error as "May@nk" is not present in myDict as a key.