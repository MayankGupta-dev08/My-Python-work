l1 = [64, 33, 79, 62, 49, 1, 48, 551, 316, 3221, 5641, 48, 6, 166]

# Using list comprehension printing  every odd indexed element of l1 expect of index1.
l2 = [l1[i] for i in range(2, len(l1), 2)]
print(l2)

# Using list enumerate() printing  every odd indexed element of l1 expect of index1.
i = 2
for i, j in enumerate(l1):
    if i % 2 == 0:
        print(j, end=" ")
