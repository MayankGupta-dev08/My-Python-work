'''Creating_CommandLineUtility_program
A command-line utility is a way of giving operating system instructions using lines of texts. Command-line programs operate via command line or PowerShell. It will interact with a command-line script.

Why?   We can call a command line program in python or any other language into a different language program easily as each program has calling support in it for calling the command lines program. So in cases, were are writing a program in some other language, but we want to perform a task in Python and call it in our program, then the command line can help us to do that.

For creating a Command Line Utility In Python, first import two modules i.e., argsparse and sys. argsparse helps us to get command-line arguments in our program, and the sys module helps us to import the code we wrote using argparse onto the console.

What is argparse?
Python comes with several different libraries that allow us to write a command-line interface for our scripts, but the standard way for creating a CLI in Python is by using the Python argparse module. The argparse module helps us to parse the arguments passed with the script and process them more conveniently. One of the advantages of using the argparse module is that it makes it easy to write user-friendly command-line interfaces.
We can use the Python argparse module to create a command-line interface by following these steps:
    Import the Python argparse module
    Create the parser
    Add optional and positional arguments to the parser
    Execute .parse_args()
When we execute .parse_args(), we will get the Namespace object that contains a simple property for each input argument received from the command line. In this tutorial, we are going to use the Argumentparser class available in the argparse module. We fill ArgumentParser with information about program arguments by making calls to the add_argument() method.

What is the sys module?
Python provides the sys module that gives us independence from the host machine Operating System and allows us to operate on an underlying interpreter, irrespective of its being a Linux or Windows Platform. With the help of the sys module, we can access system-specific parameters and functions. It provides different functions used to manipulate different parts of the Python Runtime Environment. To use the sys module, we have to import it so that it brings required sys module dependencies into our scope.
'''


import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "Something went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #Creating an object parser of class ArgumentParser() of module argparse.

    #Using the add_argument() method of class ArgumentParser() with the object, fro specifying the arguments which are to be given by the user.
    parser.add_argument('--x', type=float, default=1.0,
                        help="Enter first number. This is a utility for calculation. Please contact Mayank")

    parser.add_argument('--y', type=float, default=3.0,
                        help="Enter second number. This is a utility for calculation. Please contact Mayank")

    parser.add_argument('--o', type=str, default="add",
                        help="This is a utility for calculation. Please contact Mayank for more")

    args = parser.parse_args()
    # Parsing all arguments in the args using parse_args() method with the obj parser

    sys.stdout.write(str(calc(args)))
    # firstly calc(args) will take the arguments from the user and send it to function and get what is returned. since its not a string so we will convert it into and then using write we have printed it on the screen.

# NOTE - for running open powershell and change current directory to the directory in which the .py file is present, using cd.. or cd FolderName.
        # python .\165_creating_CommandLineUtility_program.py --x 7 --y 8 --o add
        # or 
        # python .\165_creating_CommandLineUtility_program.py --x 7 --y 8 --o mul
        # or 
        # python .\165_creating_CommandLineUtility_program.py --x 7 --y 8 --o sub
        # or 
        # python .\165_creating_CommandLineUtility_program.py --x 7 --y 8 --o div