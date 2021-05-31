# Multiplication Table for number n, where n is asked from the user.

n = int(input("Enter the number for which you want multiplication table: "))


# Using while loop for the same 
# i = 1
# while i<11:
#     print(n,"x "+str(i)+" = ", n*i)
#     i += 1

print("Printing table of "+str(n)+" : ")
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
    # print(n,"x "+str(i)+"  = ", n*(i))
    # if i ==10:
    #     break

# Printing table in reverse order.
print("\nPrinting table of "+str(n)+" in reverse order")
for i in range(10,0,-1):
    print(f"{n} x {i} = {n*i}")
    # if i == 0:
    #     break

