n = int(input("Number of elements in your tuple: "))
lst = []
for i in range(n):
    l = input("Enter your "+str(i+1)+ " Element: ")
    lst.append(l)

tup = tuple(lst)
print("Yor Tuple: " ,tup)
    