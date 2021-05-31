# creating a lists which can contain variables of any data type
a = ["Abc", 123, 88.4, True, None]

# printing the list 
print(a)
print(a[0:5])
print(a[-5:])
# printing the list after slicing
print(a[1:4])
# printing the list after advanced or skip slicing
print(a[::2])
# printing a particular element of the list 
print(a[3])

#asking for a list from user and printing it
friends = ["Ashu", "Kake", "Sumit", "Mohit", "Ankit", "Puru", "Pulkit", 84]
print(friends)
# updating the list 
friends[7] = "Divya"
print(friends)
friends.append("Mannu")
print(friends)

# Sum of elements (numbers) of a list
L = [1,56,433,67,32,122,86]
print(L[0]+L[1]+L[2]+L[3]+L[4]+L[5]+L[6]) #method1
print(sum(L)) #method2