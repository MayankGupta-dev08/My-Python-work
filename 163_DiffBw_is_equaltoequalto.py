'''
Difference b/w is and ==
is : reference equality --> two referneces referring to same object
== : value equality --> two objects having same value
'''

a = [1,2,3,5]
b = a # b is pointing to a, so both pointing to same object, so both have same value
c = [1,2,3,5] # creating new thing whose value is same as a
d = a[:] # creating a copy of a, but d is pointing to its own address

if a==b:
    print(True)
else:
    print(False)

if a is b:
    print(True)
else:
    print(False)

if a==c:
    print(True)
else:
    print(False)

if a is c:
    print(True)
else:
    print(False)

if a==d:
    print(True)
else:
    print(False)

if a is d:
    print(True)
else:
    print(False)

'''--------------OUTPUT--------------'''
# True
# True
# True
# False
# True
# False