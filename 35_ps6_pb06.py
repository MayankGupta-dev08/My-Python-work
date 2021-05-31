# Grade for a given Marks

marks = int(input("Enter your marks: "))

if marks>=90 and marks<=100:
    print("Congrats!! You are Pass\n")
    print("Your Garde is A+")
elif marks>=80:
    print("Congrats!! You are Pass\n")
    print("Your Garde is A")
elif marks>=70:
    print("Congrats!! You are Pass\n")
    print("Your Garde is B")
elif marks>=60:
    print("Congrats!! You are Pass\n")
    print("Your Garde is C")
elif marks>=50:
    print("Congrats!! You are Pass\n")
    print("Your Garde is D")
elif marks<=40 and marks>=0:
    print("Your Garde is F and You are Fail.")
else:
    print("Invalid marks enter")