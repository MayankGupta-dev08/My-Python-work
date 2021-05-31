# concatenating two strings
greetings = "Good morning, "
name = input("Enter your name: ")
text = greetings + name
print(text)

# name2 = "Mayank Gupta"
i = 0
while i<len(name):
    print(name[i])
    i += 1
print(len(name))

# String Slicing
'''Suppose t = "name"
for t[0:4], string will run from 0 -> n to 3 -> e
t[0:4] is same as t[:] or t[0:] or t[:4] or t[-5:-1]'''
print(name[0:len(name)])
print(name[1:len(name)-1])
print(text[1:(len(text)-2)])


t = "Divya"
print(t[:])
print(t[0:5])
print(t[-5:])

# t[-5:-1] is same as t[0:4]

# String Slicing with skip value
word = "playground"
print(word[::2])
print(word[::3])
print(word[::4])