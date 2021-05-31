# Renaming a file by creating a copy of the original file and deleting the original one.

import os
oldfile = "poem_copy.txt"
newfile = "renamed_by_python.txt"

f = open(oldfile, "r")
content = f.read()
f.close()
f = open(newfile, "w")
f.write(content)
os.remove(oldfile)
