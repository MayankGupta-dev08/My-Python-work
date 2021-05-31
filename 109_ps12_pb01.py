from os import read


def readFile(fileName):
    try:
        with open(fileName, "r") as f:
            print(f"File {fileName} found!!")
            print(f.read(),"\n")
    except FileNotFoundError:
        print(f"File {fileName} not found.\n")

readFile("sample.txt")
readFile("sample4.txt")
readFile("sample3.txt")