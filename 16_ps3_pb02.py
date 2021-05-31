letter = '''Dear <|NAME|>,
Greetings from ABC Construction company. We are happy to tell you about your selection.
Congrats, you are selected for the job!!
Have a great day ahead!

Thanks and regards,
ABC Construction Co.

Date: <|DATE|>'''

name = input("Enter your good name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)

print("\n",letter) #this is also correct.
# print("\n" + letter) #this is also correct.