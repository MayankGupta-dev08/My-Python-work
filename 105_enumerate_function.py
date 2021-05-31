list1 = [1.0, 63, 57, 27, "Apple", True]

# index = 0
# for i in list1:
#     print(f"{index}, {i}")
#     index +=1
#  But this could be done more sophesticately.

for i, j in enumerate(list1):
    print(f"{i}, {j}")
    # Returns firstly index and then its element, so i -> index and j -> element.

# Same result as above, so it deosn't depends on variable name.
# for index, memb in enumerate(list1):
#     print(f"{index}, {memb}")