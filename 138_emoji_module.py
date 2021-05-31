'''Different functions in emoji module'''
# <https://www.geeksforgeeks.org/python-program-to-print-emojis/> 

# Both emoji and emojis are external modules. Need to install using pip install emoji

from emoji import emojize

print(emojize(":thumbs_up:"))
print(emojize(":red_heart:")) #black heart
print(emojize(":red_heart:", variant="emoji_type")) #red heart
print(emojize(":green_heart:"))
print(emojize(":blue_heart:"))
print(emojize(":yellow_heart:"))
print(emojize(":grinning_face_with_big_eyes:"))
print(emojize(":winking_face_with_tongue:"))
print(emojize(":zipper-mouth_face:"))
print("")


import emojis
emojified = emojis.encode("There is a :snake: in my boot !")
print(emojified)
print("")


'''Using CLDR short name:'''
print("\N{face with tears of joy}")
print("\N{rolling on the floor laughing}")
print("\N{slightly smiling face}")
print("\N{winking face}")
print("\N{grinning face}")


'''Using Unicodes:
Every emoji has a Unicode associated with it. Emojis also have a CLDR short name, which can also be used.
From the list of unicodes, replace “+” with “000”. For example – “U+1F600” will become “U0001F600” and prefix the unicode with “\” and print it.'''

print("")
# grinning face
print("\U0001f600")

# grinning squinting face
print("\U0001F606")

# rolling on the floor laughing
print("\U0001F923")

