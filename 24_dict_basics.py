# Dictionary is a collection of key-value pair.

myDict = {
    "Mayank" : "Construction Manager",
    "Mridul" : "Coder",
    "Marks"  : [88, 86],
    "Dict2"  : {"Mannu":"Elder", "Puru":"Younger"},
    "H_No"   : 133
}

print(myDict)
print(myDict["Mayank"])
print(myDict["Mridul"])
print(myDict["Marks"])
print(myDict["Marks"][0])
print(myDict["Dict2"])
print(myDict["Dict2"]["Mannu"])
print(myDict["Dict2"]["Puru"])

# Updating Values of key of Dictionary.
myDict["Marks"] = [88.0, 86.0]
print(myDict["Marks"])
print(myDict)