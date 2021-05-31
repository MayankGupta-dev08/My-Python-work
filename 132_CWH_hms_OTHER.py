# Health Management System
client_dict = {1: "Harry", 2: "Rohan", 3: "Hammad"}
choice_dict = {1: "Exercise", 2: "Diet"}


def getDateTime():
    import datetime
    return datetime.datetime.now()


try:
    print("Select Client Name:")
    for key, value in client_dict.items():
        print(f"Press {key} for {value}")

    client_num = int(input())
    print("Selected Client : ", client_dict[client_num])

    print("Press 1 for Logging data")
    print("Press 2 for Retrieve data")
    op = int(input())

    if op == 1:
        for key, value in choice_dict.items():
            print(f"Press {key} for logging {value} data")

        choice_num = int(input())
        print("Selected Job : ", choice_dict[choice_num])
        f = open(client_dict[client_num] + "_" + choice_dict[choice_num] + ".txt", "a")
        k = 'y'
        while(k != "n"):
            mytext = input(f"Enter {choice_dict[choice_num]} data\n")
            f.write("[ " + str(getDateTime()) + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n: ")
            continue
        f.close()
    elif op == 2:
        for key, value in choice_dict.items():
            print(f"Press {key} to retrieve {value} data")
        choice_num = int(input())
        print(client_dict[client_num], "-", choice_dict[choice_num], "Report :")
        f = open(client_dict[client_num] + "_" + choice_dict[choice_num] + ".txt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
    else:
        print("Invalid Input !!!")
except Exception as e:
    print("Wrong Input !!!")
