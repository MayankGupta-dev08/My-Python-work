from functools import reduce

l1 = [1, 0, 10, 5, 80, 45, 66, 33, 82, 90, 40, 35, 6]
print(reduce(lambda a, b: max(a, b), l1))
