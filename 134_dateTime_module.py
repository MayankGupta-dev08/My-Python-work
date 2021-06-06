'''Using datetime module
   Two classes:
                datetime
                    Function: now() 
                date
                    Function: today()
1.  now() is used to get cuurent local time.
2.  
'''

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
print("Current time (now): ", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	



from datetime import date

tday = date.today()
print("Today's date:", tday)

# dd/mm/YY
d1 = tday.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = tday.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = tday.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = tday.strftime("%b-%d-%Y")
print("d4 =", d4)


'''---------------------Output---------------------'''
# Current time (now):  2021-06-07 00:10:40.297994
# date and time = 07/06/2021 00:10:40
# Today's date: 2021-06-07
# d1 = 07/06/2021
# d2 = June 07, 2021
# d3 = 06/07/21
# d4 = Jun-07-2021