'''List Comprehension is an elegant way of creating a list from an existing list.'''

lst1 = [1,2,3,5,6,1,5,46,456,846,6,54,213,21.5,4.5,1.68,165,4.51,876]
# lst2 = []
# for i in lst1:
#     if i>10:
#         lst2.append(i)
# print(lst2)

# Shortcut to write the above code in one line.
lst2 = [ item for item in lst1 if item>10]
print(lst2)