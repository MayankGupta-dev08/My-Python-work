# Program to mine a log file and find out whether it contains "python" or not.

content = True
i=1
with open("log.txt", "r") as f:
    while content:
        content = f.readline().lower() #Two functions simultaneously.
        if "pagal" in content:
            print(f"Yes, Pagal is present in line {i}")
            print(f"Line{i}", content)
        i+=1
