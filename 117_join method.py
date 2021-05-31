'''
Join method or bin method
works both for list and tuples
"\n".join(tuple1)
'''

list1 = ["Laptop", 'Mouse', 'Keyboard', 'Phone', 'Pendrive', 'Headphones']
# sentence = "~~~".join(list1)
# sentence = " and ".join(list1)
# print(sentence)
sentence = "\n".join(list1)
print(sentence)
print(type(sentence))

'''OUTPUT'''
# Laptop
# Mouse
# Keyboard
# Phone
# Pendrive
# Headphones
# <class 'str'>