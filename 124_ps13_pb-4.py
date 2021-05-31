# def div5(num):
#     if num%5==0:
#         return True
#     else:
#         False

l1 = [1, 0, 10, 5, 80, 45, 66, 33, 82, 90, 40, 35, 6]
# print(list(filter(div5, l1)))

# Other way
print(list(filter(lambda n: n % 5 == 0, l1)))
