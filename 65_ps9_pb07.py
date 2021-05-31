# To copy the content of a file and create a new file.

with open("poem.txt") as f:
    content = f.read()

with open("poem_copy.txt", "w") as f:
    f.write(content)
 