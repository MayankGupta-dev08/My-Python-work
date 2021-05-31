for i in range(10):
    print(i)
else:
    print("This is inside else of for.\n") #Here it will print this line after the loop.

# this will give you clear idea about this for-else
print("Example for Break keyword and also for-else statement")
for i in range(10):
    print(i)
    if(i==5):
        break
else:
    print("This is inside else of for.") #here it will not print this line after the loop as the loop is not successfully terminated rather it is forcefully terminated or interrupted by break statement.

print("\nExample for Continue keyword")
for i in range(10):
    if(i==5):
        continue
    print(i)