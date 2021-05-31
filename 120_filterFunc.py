'''FILTER FUNCTION RETURNS ALL THE VALUES OF A LIST FOR WHICH A FUNCTION RETURNS TRUE AND NOT FALSE.
i.e. STORES THOSE WHO WILL GIVE RESULT AS TRUE.
Function name is passed as an argument along with the list in filter(func1, inpList)
Result is to be typecasted into a list.
a = list(filter(func1, inpList))'''


def less10(num):
    if num < 10:
        return True
    else:
        return False

g25 = lambda num:num>=25 #g25 is a function written using lambda function.
l1 = [1, 3, 5, 7, 9, 25, 55, 98, 33, 45, 66]
print(list(filter(less10, l1)))
print(list(filter(g25, l1)))
