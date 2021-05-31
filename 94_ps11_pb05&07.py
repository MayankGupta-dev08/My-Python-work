'''Adding two vectors and their dot product'''

class Vector_nD:
    def __init__(self, l):
        self.lst = l

    def __add__(self, v):
        l3 = []
        for i in range(len(self.lst)):
            l3.append(self.lst[i] + v.lst[i])
        return Vector_nD(l3)

    def __mul__(self, v):
        dotProduct = 0
        for i in range(len(self.lst)):
            dotProduct += (self.lst[i] * v.lst[i])
        return dotProduct

    def __str__(self):
        str = ""
        index = 0
        for i in self.lst:
            str += f" {i}a{index} +" # Way of adding data in a string.
            index += 1
        return str[:-1] # str[:-1], for eleminating the last element which is '+' symbol.

    def __len__(self):
        return len(self.lst)   

n = int(input("Enter the dimension for your vectors: "))
print("")
l1 = []
l2 = []
for i in range(n):
    m1 = int(input(f"Enter member{i+1} of vector1: "))
    l1.append(m1)
print("")
for j in range(n):
    m2 = int(input(f"Enter member{j+1} of vector2: "))
    l2.append(m2)
    
v1 = Vector_nD(l1)
v2 = Vector_nD(l2)

print("Vector1", v1)
print("Length of Vector1", len(v1))
print("Vector2", v2)
print("Length of Vector2", len(v2))
v3 = v1+v2 # v3 is being returned as an object, so it will use __str__ to print.
v4 = v1*v2 # v4 is being returned as an integer, it will use it's value.
print("Addition of your two vectors: ", v3)
print("Dot product of your two vectors: ", v4)