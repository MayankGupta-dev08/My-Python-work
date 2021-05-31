# Write a program to find out whether a student is pass or fail, if it requires total of 40% and at least 33% in each subject to pass. Assume 3 subjects and ask marks as an input from the user. 

# n = int(input("Enter total number of subjects: "))
# RecordDict = {}
# f = 34
# for i in range(n):
#     k = input("Enter name of Subject"+str(i+1)+" : ")
#     v = int(input("Enter marks (out of 100) of that subject"+str(i+1)+" : "))
#     RecordDict.update({k:v})
#     f = min(f, v)
# print("\n", RecordDict, "\n")

# marks = list(RecordDict.values())
# print(marks)
# print(type(marks))

# percent = (sum(marks)/n)*100
# if (f<=33):
#     print("You Fail")
# elif (percent <40):
#     print("You Fail")
# else:
#     print("You Pass")

n = int(input("Enter total number of subjects: "))
RecordDict = {}
fail_subjects = {}

for i in range(n):
    k = input("Enter name of Subject"+str(i+1)+" : ")
    v = int(input("Enter marks (out of 100) of that subject"+str(i+1)+" : "))
    RecordDict.update({k:v})
    if v < 34:
        fail_subjects[k] = v
print("\nThis is what you mentioned: ", RecordDict, "\n")

marks = list(RecordDict.values())
print("This is the list of your marks: ",marks)
# print(type(marks))
total = (sum(marks)/n)
# print("Total % of your marks is: ", total, "\n") #this is also correct
# Below line is used for printing only 2 digits of total% after the decimal.  
print("Total % of your marks is: {:.2f}".format(total))

if (len(fail_subjects)>0):
    print("You Fail in the following subjects: ")
    print(fail_subjects,)
elif (total <40):
    print("You Fail since total% < 40%")
else:
    print("Congrats!!, You Pass")
