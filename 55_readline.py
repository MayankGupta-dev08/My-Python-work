'''55_FileHandling'''

# Printing one line at a time using readline() function. 
f = open("sample.txt") 
data = f.readline()
print(data)
data = f.readline()
print(data)
data = f.readline()
print(data)
data = f.readline()
print(data)
f.close()

# Partially reading a line after reading a line completely.
f2 = open("sample2.txt") 
data2 = f2.readline() # Read 1st line completely.
print(data2)
data2 = f2.readline(4) # Read first 4 words of 2nd line.
print(data2)
data2 = f2.readline() # Reading, starting from where left ie. 5th word of 2nd line and continueing 
print(data2)
data2 = f2.readline()
print(data2)
f2.close()

