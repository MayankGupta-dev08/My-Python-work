'''Creating a generator function for generating an infinite stream of even numbers and then printing first 10.'''
# NOTE - Use yield and next()

def evenNum_genr():
    n1 = 0
    while True:
        yield n1
        n1 += 2

series = evenNum_genr()
for i in range(0,10):
    print(next(series), end=" ")
print("\n")


'''Generator Comprehension is an elegant way of creating a list from an existing list.'''

even = (i for i in range(101) if i%2==0)

print(type(even))
print(even, "\n")

print(even.__next__(), end=" ")
print(even.__next__(), end=" ")
print(even.__next__(), end=" ")
print(even.__next__(), end=" ")
print(even.__next__(), end=" ")
print(even.__next__(), end=" ")
print(even.__next__(), end=" ")
print(even.__next__(), end=" ")
print(even.__next__(), end=" ")
print(even.__next__(), end=" ")