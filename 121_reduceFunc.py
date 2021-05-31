'''reduce function applies a rolling computation to sequetial pair of elements using a function and a list
Before using reduce function, we need to import it using following line - 
from functools import reduce
Syntax: a = reduce(func1, inpList)
No need to convert this as a list as it will return a single value'''

from functools import reduce

lst1 = [1,2,3,4,5]
summation = lambda a,b: a+b
val1 = reduce(summation, lst1)
print("Val1: ",val1)

n=6 #Number for which u want factorial, we can take as an imput from user also.
lst2 =[i for i in range(1,n+1)]
print(lst2)
# lst2 = [1,2,3,4,5,6]
fact = lambda a,b: a*b
val2 = reduce(fact, lst2)
print("Val2: ", val2)
