'''
In Python's re module to work with RegEx
A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.
Functions in modules
                    re.findall(), re.search(), re.sub(), re.split(), re.subn(), re.finditer()

raw string - consider as it is what is given.
        rawstr = r"\n"
        print(rawstr) --> \n

findall:    It finds all search for matches and print resultant in the form of a list, if nothing than returns empty list.
search:     It works the same as a findall, but the resultant is a matched object, if any found, if nothing than returns None.
split:      The split function splits the string from every matched into two new strings.
sub:        The sub-function works exactly like a replace function in notepad or MS Word, it replaces the original word, with a word of our choice.
finditer:   The finditer yields an iterator as a resultant with all the objects that match the one we sent it) finditer supports more attributes than any other function defined above. It also provides more details related to the matched object.

Meta Characters
[]      A set of characters
\       Signals a special sequence (can also be used to escape special characters)
.       Any character (except newline character)
^       Starts with
$       Ends with
*       Zero or more occurrences
+       One or more occurrences
{}      Exactly the specified number of occurrences
|       Either or
()      Capture and group

Special Sequences
\A      Returns a match if the specified characters are at the beginning of the string
\b      Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
\B      Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
\d      Returns a match where the string contains digits (numbers from 0-9)
\D      Returns a match where the string DOES NOT contain digits
\s      Returns a match where the string contains a white space character
\S      Returns a match where the string DOES NOT contain a white space character
\w      Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
\W      Returns a match where the string DOES NOT contain any word characters
\Z      Returns a match if the specified characters are at the end of the string


The Match object has properties and methods used to retrieve information about the search, and the result:
    .span() returns a tuple containing the start-, and end positions of the match.
    .string returns the string passed into the function
    .group() returns the part of the string where there was a match

'''

import re
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''

# NOTE - Use of finditr

# Meta Characters
# patt = re.compile(r'fass')
# patt = re.compile(r'.adm')
# patt = re.compile(r'adm.')
# patt = re.compile(r'^Tata')
# patt = re.compile(r'iin$')
# patt = re.compile(r'ai*')
# patt = re.compile(r'a*i*')
# patt = re.compile(r'ai+')
# patt = re.compile(r'ai{2}')
# patt = re.compile(r'(ai){1}')
# patt = re.compile(r'ai{1}|Fax')


# Special Sequences
# patt = re.compile(r'\ATata')
# patt = re.compile(r'\bFax')
# patt = re.compile(r'Fax\b')
# patt = re.compile(r'27\b')
# patt = re.compile(r'\d{5}-\d{4}')
patt = re.compile(r'\d{5}-\d{4}')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
    print(type(match))


txt = "The rain in Spain falls mainly in the plain and nearly 6 times a month in monsoon."
x = re.search("^The.*Spain$", txt)
print(x)
print(type(x))

y = re.findall("^The.*monsoon$", txt)
print(y)
print(type(y))

#Check if the string ends with "Spain":
x0 = re.findall("monsoon\Z", txt)
print(x0)

#Find all lower case characters alphabetically between "a" and "m":
z = re.findall("[a-m]", txt)
print(z)

txt1 = "hello world, hello. Hello hello"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x1 = re.findall("he..o", txt1)
print(x1)

#Check if the string contains "ai" followed by 0 or more "x" characters:
x2 = re.findall("aix*", txt)
print(x2)

#Check if the string contains "ai" followed by 1 or more "x" characters:
x3 = re.findall("aix+", txt)
print(x3)

#Check if "ain" is present, but NOT at the beginning of a word using \B:
x4 = re.findall(r"\Bain", txt)
print(x4)

#Check if "ain" is present, but NOT at the end of a word using \B:
x5 = re.findall(r"ain\B", txt)
print(x5)

#Return a match at every no-digit character:
x6 = re.findall("\D", txt)
print(x6)

#Return a match at every digit character:
x7 = re.findall("\d", txt)
print(x7)

#Return a match at every white-space character:
x8 = re.findall("\s", txt)
print(x8)


# USEAGE OF SETS and some examples
txt = "The rain in Spain"

# Check iuse of setsf the string has any a, r, or n characters:
y1 = re.findall("[arn]", txt)
print(y1)

#Check if the string has any characters between a and n:
y2 = re.findall("[a-n]", txt)
print(y2)

# Check if the string has characters except a, r, or n:
y3 = re.findall("[^arn]", txt)
print(y3)


text = "8 times before 11:45 AM"

#Check if the string has any digits:
y4 = re.findall("[0-9]", text)
print(y4)

#Check if the string has any two-digit numbers, from 00 to 59:
y5 = re.findall("[0-5][0-9]", txt)
print(y5)

#Check if the string has any characters from a to z lower case, and A to Z upper case:
y6 = re.findall("[a-zA-Z]", txt)
print(y6)

#Check if the string has any + characters:
y7 = re.findall("[+]", txt)
print(y7)

# Use of re.split() function, returns a list where the string has been split at each match:
txt = "The rain in Spain"



# Split at each white-space character:
t1 = re.split("\s", txt)
print(t1)
# Split the string only at the first occurrence:
t2 = re.split("\s", txt, 1)
print(t2)




# The sub() function replaces the matches with the text of your choice:

txt = "The rain in Spain"
# Replace every white-space character with the number 9:
x = re.sub("\s", "9", txt)
print(x)
# Replace the first 2 occurrences:
x = re.sub("\s", "9", txt, 2)
print(x)



# NOTE - EXAMPLE OF USING THE MATCH OBJECT AND ITS FUNCTIONS
import re

txt = "The rain in Spain"

x = re.search(r"\bS\w+", txt)
print(x)
print(x.span())
print(x.string)
print(x.group())