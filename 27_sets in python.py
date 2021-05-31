'''SETS - It is a collection of non repetitive elements, immutable, unordered and unindexed.'''

a = {1,2,3,4,1,5,5,6,7,3}
print("A set: ", a)
print(type(a))

# Another way of defining sets in python
# Note: this will create an empty dictionary and not an empty set.
b = {}
print("\n Empty Dict: ", b)
print(type(b))

# An empty set can be created by the following syntax:
c = set()
print("\n Empty Set: ", c)
print(type(c), "\n")

'''SET METHODS'''

# Adding elements in the empty set
c.add(4)
c.add(6)
c.add(6)
c.add(8)
c.add(8)
c.add(10)
c.add(10)
print(c, "\n") #Sets are also unordered just like dictionaries, and can be defined using {} like dictionary, but it is not a collection of key value pair.

# Lists AND Dictionary can't be added in a set, but tuples can be added becoz just like tuples, sets are also immutable where as Lists and Dictionary are both mutuable.
c.add((5, 7, 9))
print(c)
# c.add([5,7]) #this throws an error.
# c.add({5:3,7:"abc"}) #this throws an error.

print("length of the set: ", len(c))
c.remove(8) #removes 8 from the set
# c.remove(18) #gives an error messages as 18 is not in the set and we are trying to removes it from the set.
print(c)
print("Removing a random element from the set: " ,c.pop())
print(c)
print(c.clear())
print(c)

# A num can coexist in a set as an int and a str simultaneously, but int and float of 18 whcih is 18 and 18.0 can't.
d = {"18", 18, 18.0}
print("\nPrinting 18 as a str and as int in a set: ", d, "\n")

'''UNION and INTERSECTION in SETS'''

s1 = {1,8,56,9,10,7,56}
s2 = {1,8,85,6,33,9,6,66}

print(s1)
print(s2)
print(s1.union(s2)) #returns the union of s1 and s2 = {1,8,56,9,10,7,85,6,33,9,66}
print(s1.intersection(s2)) #returns the intersection of s1 and s2 = {1,8,9}
print(s1.difference(s2)) # s1-s2 = {56,10,7}
print(s2.difference(s1)) # s2-s1 = {85,6,33,66}
