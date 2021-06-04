'''
lambda functions or anonymus functions
generally used for functions which are simple and 2 to 3 liners.
function name = lambda arg: return parameter
'''

# def func(a):
#     return a+5

a = 8
func = lambda a:f"Sum of {a}+5: {a+5}"
square = lambda x:x*x
sum = lambda x,y,z: x+y+z
print(func(a))
print(square(6))
print(sum(a,65,6))
