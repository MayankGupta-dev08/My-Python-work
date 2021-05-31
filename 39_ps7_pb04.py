# prime number
num = int(input("Enter the number to be checked for prime\n"))
p = 0
if num==1:
        print("Not Prime")
else:        
    for i in range(2,num):
        if (num%i == 0):
            p = p + 1
            break

    if (p==0):
        print("Prime")
    else:
        print("Not Prime")