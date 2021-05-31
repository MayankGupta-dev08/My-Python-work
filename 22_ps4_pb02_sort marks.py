# write a programe to accept 6 students marks and sort them.

# Method 1
StudentMarks = []
for i in range(6):
    m = input("Enter marks of Student"+ str(i+1) +" : ")
    m = int(m)
    StudentMarks.append(m)
    # print(StudentMarks)

print("Sorted list of Student Marks is:-")
StudentMarks.sort()
print(StudentMarks)