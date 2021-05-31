'''Dictionary Comprehension is an elegant way of creating a list from an existing list.
Also, remember set doesn't contain duplicate elements.
'''

# Python code to demonstrate dictionary creation using list comprehension
myDict1 = {x: x**2 for x in [1,2,3,4,5]}
print (myDict1)


# Python code to demonstrate dictionary comprehension
# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]
# but this line shows dict comprehension here  
myDict2 = { k:v for (k,v) in zip(keys, values)}  
# We can use below too
# myDict = dict(zip(keys, values))  
print (myDict2)


# Python code to demonstrate dictionary comprehension using if.
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)


# One more example
sDict = {x.upper(): x*3 for x in 'coding '}
print (sDict)


# dictionary comprehension example
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)


#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dollar_to_pound = 0.76
new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(new_price)

