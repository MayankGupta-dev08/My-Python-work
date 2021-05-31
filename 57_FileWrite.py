'''57_FileHandling'''
# Write ("w") or Append ("a") Mode if used, will create a new file if it already does not exist.
# "w" mode - writes from the begining.
# "a" mode - writes from the end of the last char (if any).

f1 = open("AnotherFile.txt", "w")
f1.write("This is the first line, I am writing in this file!!\n")
# text = f1.read() # This will not work in write mode.
# print(text)
f1.close()

f2 = open("AnotherFile.txt", "a")
f2.write("Hi, I am adding a new line to this.\n")
f2.write("This is nice.")
# text = f2.read() # This will not work in append mode.
# print(text)
f2.close()

f2 = open("AnotherFile.txt", "r")
text = f2.read()
print(text)
f2.close()