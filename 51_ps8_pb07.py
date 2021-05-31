# Function to remove a word from the string and strip of the extra spaces from string at the same time.

def str_rem_strip(str,word):
    new_str = str.replace(word, "&")
    return new_str.strip()

s1 = "      Mayank is a hardworking and intelligent boy         "
print(str_rem_strip(s1, "and"), ".")

# txt = "     banana     "

# x = txt.strip()

# print("of all fruits", x, "is my favorite")