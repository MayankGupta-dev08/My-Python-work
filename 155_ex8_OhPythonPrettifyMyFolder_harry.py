'''
Oh Python prettify my folder

make a func ->  def Soldier (path, filename, exten)
    path = path of folder to be prettified
    filename = noChange.txt, File Name Which Contain Name Of Files which are Not to be Altered
        since other files or folder's first alphabet will be capitalized
    exten = .jpg or .png, These files will be renamed from 0 to n number of such files.
'''

import os

def soldier(path, fileNoChange, ext):
    os.chdir(path) # Change the directory to that directory
    files = os.listdir(path) # returns the name of all files or folder in a list
    i =1 # for renaming files of given extensions
    with open(fileNoChange) as f:
    # Reading that file which has names of files which are not to be altered.
        fileNCL = f.read().split("\n")
        # Created a new list having names of files which are not to be altered.

    for file in files:
        if  file not in fileNCL:
            os.rename(file, file.capitalize())
        
        if os.path.splitext(file)[1] == ext:
        # This will return the name of extension in tuple format so get it we have used index 1.
            os.rename(file, f"{i}{ext}")
            i += 1

if __name__ == "__main__":
    try:    
        path = input("Enter the path of the folder which you want to prettify\n")
        # C:\Users\cemay\OneDrive\Desktop\New folder
        fileNoChange = input("Enter the name of the file .txt in which names are mentioned\n")
        # C:\Users\cemay\OneDrive\Desktop\New folder (2)\abc.txt
        ext = input("Enter the extension: ")
        # soldier(r"C:\Users\cemay\OneDrive\Desktop\New folder", r"C:\Users\cemay\OneDrive\Desktop\New folder\abc.txt", ".jpg")
        soldier(path, fileNoChange, ext)
        # BOth methods will work, giving directly or input from user.
    except:
        print("Somthing went wrong!")