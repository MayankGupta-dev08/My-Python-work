'''Set Comprehension is an elegant way of creating a set from an existing list or set.
Also, remember set doesn't contain duplicate elements.
'''

set1 = {1,2,3,5,6,1,5,46,456,846,6,54,213,21.5,4.5,1.68,165,4.51,876}
# set2 = set()
# for i in set1:
#     if i>10:
#         set2.add(i)
# print(set2)

# Shortcut to write the above code in one line.
set2 = {i for i in set1 if i>10}
print(set2)
print(type(set2), "\n\n")


marks = {m1 for m1 in [55,42,66,33,85,94,40,21,44,55,66,] }
print(marks)
print(type(marks))