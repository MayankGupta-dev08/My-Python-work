# l1 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
n = int(input("Enter the number for getting its table: "))
l1 = [str(n*i) for i in range(1,11)]
# We have converted the n*i from int to str becausejoin accepts str elements to join.

# METHOD 1
str_vert = "\n".join(l1)
print(str_vert)

# METHOD 2
print("")
for i, j in enumerate(l1):
    print(f"{n} x {i+1} = {j}")