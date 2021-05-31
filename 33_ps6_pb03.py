'''A spam comment is defined as a text containg the following words.
"make a lot of money", "buy now", "subscribe this", "make money", "lottery", "jackpot", "click this".
Write a program to detect these spams.'''

text = input("Enter the text to check whether it is a spam or not\n")
text = text.lower()

# if ("make a lot of money" in text):
#     spam = True
# elif ("buy now" in text):
#     spam = True
# elif ("subscribe this" in text):
#     spam = True
# elif ("make money" in text):
#     spam = True
# elif ("lottery" in text):
#     spam = True
# elif ("jackpot" in text):
#     spam = True
# elif ("click this" in text):
#     spam = True
# else:
#     spam = False

spam = False
list1 = ["make a lot of money", "buy now", "subscribe this", "make money", "lottery", "jackpot", "click this"]
for i in list1:
    if i in text:
        spam = True
        break
    
if (spam):
    print("This text is spam")
else:
    print("This text is not spam")