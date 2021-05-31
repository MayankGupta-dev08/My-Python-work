# Write a program to create .txt files for Multiplication of Tables from 2 to 20 and store it in folder named tables2_20.

for i in range(2,21):
    with open(f"tables2_20/Multiplication Table of {i}.txt", "w") as f:
        for j in range(1,11):
            f.write(f"{i}x{j}={i*j}")
            if j!=10:
                f.write("\n")