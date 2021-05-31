# l1 = ["Saurav", "Sachin", "Rahul", "Kholi", "Dhoni"]
l1 = []
m = int(input("No. of names to be entered: "))
for j in range(m):
    # name = input("Enter name"+str(j+1)+" : ") #This is also correct.
    name  = input(f"Enter name {j+1} : ") #This is known as f-string format and this makes easy writing of expression when both sting and int are there in input or print function.
    l1.append(name)
print(l1)

for i in l1:
    # if (i[0] == 's' or i[0] == 'S'): #This is also correct.
    if (i.startswith("S") or i.startswith("s")):
        print("Hello!!, ", i)