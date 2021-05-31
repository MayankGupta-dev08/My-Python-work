# working with tuples and creating with () - tuples can't be changes once created.

# creating a tuple
t1 = () #creating an empty tuple
print(t1)
t2 = (1,) #creating a tuple with single element
# t2 = (1) is the wrong way to create tuple with single element 
print(t2)

t3 = (1, 2, "HArry", "Mayank", False, None, 84.4)
print(t3)
print(t3[0])
print(t3[1:3])
print(t3[::2])

# a tuple can't be updated, so the below line is invalid.
# t3.append(55)
# or t3[0] = "john" - throws an error as tuple can't be updated

t4 = (1, 2.4, 3, 4.8, 1, 5, 6, 1, 7)
print(t4)
print(t4.count(1)) # retuns the count of the element.
print(t4.index(5)) #gives the index value of the element.


tup = ('physics', 'chemistry', 1997, 2000)
print (tup)
del tup
print ("After deleting tup : ")
print(tup)

