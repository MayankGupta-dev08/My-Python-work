import os

# print(dir(os))

print(os.getcwd())

os.chdir("D:\Mayank\Coding")    
print(os.getcwd(),"\n")
os.chdir("D:\Mayank\Coding\python\Code_with_Harry\One Video Course")    

print(os.listdir("D:\Mayank\Coding\python"),"\n")

os.mkdir("Created using mkdir")
os.makedirs("Created_using/makedirs")
with open("Created_using/makedirs/New file.txt", "w") as f:
    f.write("This is a new file created using python")

os.rename("mylog.txt", "myLog.log")

print(os.path.exists("D:\Mayank\Coding\python"))
print(os.path.isdir("D:\Mayank\Coding\python"))
print(os.path.isfile("D:\Mayank\Coding\python"))
print(os.path.isfile("D:\Mayank\Coding\python\Code_with_Harry\One Video Course\AnotherFile.txt"))
