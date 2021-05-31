'''56_FileHandling'''
# By this way, we can read the same file differently, in a program multiple times, by creating different objects to read, here -> f1,f2. 

f1 = open("sample.txt") 
data = f1.read() #read whole file.
print(data)
f1.close()

# Reading same file partially, using f2 instead of f1.

f2 = open("sample.txt") 
data = f2.read(5)
print(data)
data = f2.read(10)
print(data)
f2.close()
