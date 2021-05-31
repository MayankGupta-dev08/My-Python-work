'''File Handling'''
'''With Statement --> Context Manager
No need to write f.close() when using with statement as it is done automatically.
'''

with open("AnotherFile.txt", "r") as f:
    a = f.read() #we can read write store and print the text.
    print(a) #printing whatever was earlier in file.
with open("AnotherFile.txt", "w") as f:
    f.write("This is new!!") 
    #In write mode we can't read and print the text, we can only write from the begining.
    b = f.write("oh!!") #Here only count of char in "" is stored in b.
print(a) #Although, now the file contains --> This is new!!oh!!, but it will print what it had stored earlier.
print(b) # 4 --> count of chars in oh!!
