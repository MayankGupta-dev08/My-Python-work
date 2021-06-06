import re

with open("phonebook.txt", "r") as f:
    str = f.read()

# print(str)

# NOTE - This will give all the possible matches but in match object type format
# pattern = re.compile(r"\W{1}91\d{10}")
# matches = pattern.finditer(str)
# for match in matches:
#     print(match)

# NOTE - This will only give last found result
# pattern = re.search(r"\W{1}91\d{10}", str)
# print(pattern.group())

# NOTE - This will only give last found result
# pattern = re.findall(r"[+]91\d+", str)
pattern = re.findall(r"\W{1}91\d{10}", str)
print(pattern)