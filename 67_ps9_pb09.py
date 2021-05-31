# Program to wipe out the contents of a file.

file = input("Enter name of file1 (Always end with .txt): ")
f = open(file, "w")
f.write("")
f.close()
