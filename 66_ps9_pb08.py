# To check if both the files are identical or not in terms of their content.

file1 = input("Enter name of file1 (Always end with .txt): ")
file2 = input("Enter name of file2 (Always end with .txt): ")

with open(file1) as f1:
    content1 = f1.read()
    with open(file2) as f2:
        content2 = f2.read()
        if content1 == content2:
            print("Yes, both the files are identical")
        else:    
            print("No, both the files are not identical")
