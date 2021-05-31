try:
    n = int(input("Enter the number for which you want table: "))
    l1=[n*i for i in range(1,11)]
    print(l1)
    for i,j in enumerate(l1):
        print(f"{n} x {i+1} = {j}")
except Exception as e:
    print(e)
finally:
    print("Thanks for using this code :)")
