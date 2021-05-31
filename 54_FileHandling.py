'''54_FileHandling'''
# using "sample.txt" file in the for file-handling purpose. 

# Note: if file is in same folder then just using name we can acess it, but if it is somewhere else on the computer than we have to write full path of it along with name at end instead of just name to acess it. 

# f = open("sample.text", r) 
#Here, f will become the object of this file, thru which we can perform various operations on this file.
f1 = open("sample.txt") #By default, it opens for read only.
data = f1.read()
# data = f.read() will read the full file, where as f.read(8) will read only first 8 characters of the file and give it to data variable.
print(data)
data2 = f1.read(10)
# Once a file is full read then it can't be partially read, so the above line is of no use, and data 2 will have no value or blank line.
print(data2)
# This will print a blank line only.
f1.close()

# TRYING other way round, first partially and then fully.
f2 = open("sample2.txt")
d1 = f2.read(10)
print(d1)
d2 = f2.read()
print(d2)
f2.close()
# this will also give similar result ie. it will read full file and print it. the only difference b/w this and above is, it will not print a blank line at the end.

# So a file can be read partially only if it is not read completely anywhere in the code. 

# CORRECT way of partially reading the file.
f3 = open("sample3.txt")
d = f3.read(10) #after reading first 10 char, f3 will jump to 11.
print(d) #prints first 10 only.
d = f3.read(7) #it starts reading from 11th char of first line if any, and then prints the reaming character from the second line(if any).
print(d)
d = f3.read(9)
print(d)
f3.close()