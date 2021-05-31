# This programme is written to detect the double spaces in a string.

str = '''This is a line which contain double  spaces.'''
doubleSpaces = str.find("  ")
print("Position of double spaces in the string is: ",doubleSpaces)

# This programme is written to replace the double spaces with single space in a string.

str = '''This is a line which contain double  spaces.  ok!!'''
str = str.replace("  ", " ")
print(str)