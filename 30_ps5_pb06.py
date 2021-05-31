FrndsDict = {}
n = int(input("Enter number of friends: "))
for i in range(n):
    k = input("Enter name of friend"+str(i+1)+" : ")
    v = input("Enter fav language of friend"+str(i+1)+" : ")
    FrndsDict.update({k:v})
print("\n", FrndsDict, "\n")

fav = input("Name of the friend whose fav language you want to know: ")
print(FrndsDict.get(fav))
