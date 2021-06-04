'''Dictionary Comprehension is an elegant way of creating a dictionary from an existing list or dict.
Also, remember dictionay doesn't contain duplicate keys, so no two keys will be same in a dict, if we try then it will update the value of the prev key.
'''

# Python code to demonstrate dictionary creation using list comprehension
myDict1 = {x: x**2 for x in [1,2,3,4,5]}
print (myDict1, "\n")


# Python code to demonstrate dictionary comprehension Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]
# but this line shows dict comprehension here  
myDict2 = { k:v for (k,v) in zip(keys, values)}  
# We can use below too
# myDict = dict(zip(keys, values))  
print (myDict2, "\n")


# Python code to demonstrate dictionary comprehension using if.
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict, "\n")


# One more example
sDict = {x.upper(): x*3 for x in 'coding '}
print (sDict, "\n")


# dictionary comprehension example
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict, "\n")


#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dollar_to_pound = 0.76
new_price = {key: value*dollar_to_pound for (key, value) in old_price.items()}
print(new_price, "\n")


# creating dict having {5:"item5",10:"item10"....... upto 50}
dict_n = {i: f"item{i}" for i in range(1,51) if i%5==0}
print(dict_n, "\n")

# creating another dictionary from already created dict just by switching off the key and value with each other.
dict_n1 = {i: f"item{i}" for i in range(1,8)}
print(dict_n1, "\n")
dict_n2 = {v:k for k,v in dict_n1.items()}
print(dict_n2)