'''USING time Module
function1 - time.time()
returns the number of seconds passed from some specific time

function2 - time.sleep()
ask the complier to wait/sleep fro the specified seconds before executing the next line 

function3 - time.asctime(time.localtime(time.time()))
returns the current local time '''

import time

initial_time = time.time() # cALC THE TIME TAKEN TILL NOW
k=0
while k<5:
    print("printing ",k+1)
    time.sleep(1)
    k +=1
print("While loop ran in ", time.time() - initial_time, " seconds")
# tHE ABOVE LINE CALC TIME TILL NOW - INITAL TIME

initial_time2 = time.time()
for i in range(5):
    print("printing ",i+1)
    time.sleep(1)
print("fOR loop ran in ", time.time() - initial_time2, " seconds")

localTime = time.asctime(time.localtime(time.time()))
print("")
print("Using time.asctime(time.localtime(time.time()))")
print(localTime)
