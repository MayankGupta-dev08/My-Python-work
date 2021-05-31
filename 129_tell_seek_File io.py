'''
IN FILE HANDLING
f.tell() - RETURNS THE POSITION OF FILE POINTER f in the file.
f.seek(20) - TAKES THE FILE POINTER f TO THE GIVEN POSITION in the file, here its will be 20.
'''

with open("poem.txt", "r") as f:
    print(f.tell())
    print(f.readline()) 
    print(f.tell())
    print(f.readline()) 
    print(f.seek(45))
    print(f.readline()) 
    print(f.tell())
    print(f.readline()) 
    print(f.tell())

'''OUTPUT'''
# 0
# Twinkle, twinkle, little star,

# 32
# How I wonder what you are! 

# 45
# what you are!

# 60
# Up above the world so high,

# 89