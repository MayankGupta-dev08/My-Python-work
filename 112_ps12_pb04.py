while True:
    try:
        a = int(input("Enter the Numerator for a/b: "))
        b = int(input("Enter the Denominator for a/b: "))
        if a==0 and b==0:
            print("0/0 Error")
        else:    
            c= a/b
            print(f"{a}/{b} = {c}")
            break
    except ZeroDivisionError as e:
        print(f"{a}/{b} = Infinite")
        break
    except ValueError as e:
        print("Invalid Input, try again\n")
    else:
        print("Thanks for using this code :)")
        break