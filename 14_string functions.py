story = '''the WISE MAN - 
        People have been coming to the wise man, complaining about the same problems every time.
        One day he told them a joke and everyone roared in laughter.
        After a couple of minutes, he told them the same joke and only a few of them smiled.
        When he told the same joke for the third time no one laughed anymore.
        The wise man smiled and said:
        “You can’t laugh at the same joke over and over. So why are you always crying about the same problem?”

        Moral of the story:
        Worrying won’t solve your problems, it’ll just waste your time and energy.'''

# STRING FUNCTIONS
# print(len(story))
# print(story.endswith("energy."))
# print(story.count("the"))
# print(story.capitalize()) #Return a capitalized version of the string. More specifically, make the first character have upper case and the rest lower case.
# print(story.find("People"))
# print(story.replace("wise","fool"))


#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

# this is an example of using carriage return '/r', which carries all the string written after it to the begining by replacing the starting string element of size equal to it.
txt = "Hee, this line will not be printed!!!\rWorld!!!"
print(txt) 

# for printing the ASCI vales of the alphabets
print(ord("A"))
print(ord("Z"))
print(ord("a"))
print(ord("z"))

# Python3 program to demonstrate the use of
# strip() method 
 
string = """    geeks for deks cheeks    """
 
# prints the string without stripping
print(string)
 
# prints the string by removing leading and trailing whitespaces
print(string.strip())  
 
# prints the string by removing geeks
print(string.strip(' geeks'))