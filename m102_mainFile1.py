'''For creating files which can be imported as a module, it's mandatory that their name should start with 'm', for example = m103_mainFile2.py'''

def greet(name):
    print("Good morning, ", name)

print(__name__)
# The above line prints whether this program is executed from the file where it is written i.e. from its own main file, that's why __main__ and some other file is using this file's function , then this line will show the name of this file.
if __name__ == "__main__":
    # The above line prevents the contents below it to be executed if some other file is importing the contents of this file, so it will import other things nut not the ones which are under this if statement.
    n = input("Enter a name\n")
    greet(n)