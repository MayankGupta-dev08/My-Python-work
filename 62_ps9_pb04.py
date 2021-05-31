# CENSORING a word in .txt file

with open("sample3.txt", "r") as f:
    char = f.read()

char = char.replace("donkey", "@%^%#!*&")

with open("sample3.txt", "w") as f:
    f.write(char)
