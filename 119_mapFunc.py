'''Map function - applies a function to all the items of an input list.
function name is passed as an argument along with the list in map(func1, inpList)
Result is to be typecasted into a list.
a = list(map(func1, inpList))'''

def square(num):
    return num*num


l1 = [1, 3, 5, 7, 9]

# Method 1
l2 = []
for i in l1:
    l2.append(square(i))
print(l2)

# Method 2
a = map(square, l1)
# We have to typecast the output of map function into a list
print(list(a))
# print(list(map(square, l1)))
