# CENSORING a words from a list in .txt file

words = ["mote","kaddu","ghadhe","buddhu","pagal","donkey",]

with open("sample3.txt", "r") as f:
    char = f.read()

for word in words:
    char = char.replace(word, "@%^%#!*&")

with open("sample3.txt", "w") as f:
    f.write(char)
