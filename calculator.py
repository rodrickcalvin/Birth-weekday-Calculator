#NAME --- WAMALA RODRICK CALVIN
#REG NO. ---- 16/U/12277/PS
#STUDENT NO. ---- 216012196
#COURSE ---- COMPUTER ENGINEERING

import calendar        #using the inbuilt calendar module

M = input("What is your name?\n")

a = input("Which year were you born?\n")

b = input("Enter your month of birth:\tFor January enter 1\n    February    2\n    March       3\n    April       4\n    May         5\n    June        6\n    July        7\n    August      8\n    September   9\n    October    10\n    November   11\n    December   12\n\n\n")

c = input("Enter the date on which you were born (1-30(31))\n")

x = calendar.weekday(year = int(a), month = int(b), day = int(c)) 
#using the calendar module, a function weekday is used and the inputs are assigned to their specific parameters as inputs declare


for d in c:
    if int(c) == 1:
        d = c +"st"
    elif int(c)==2:
        d = c +"nd"
    elif int(c)==3:
        d = c +"rd"
    elif int(c) >= 4 and int(c) <= 20:
        d = c +"th"
    elif int(c)==21:
        d = c +"st"
    elif int(c) == 22:
        d = c +"nd"
    elif int(c) == 23:
        d = c +"rd"
    elif int(c) == 31:
        d = c +"st"
    else:
        d = c+"th"


if int(b) == 1:
       m = "January"
elif int(b) == 2:
        m = "February"
elif int(b) == 3:
        m = "March"
elif int(b) == 4:
        m = "April"
elif int(b) == 5:
        m = "May"
elif int(b) == 6:
        m = "June"
elif int(b) == 7:
        m = "July"
elif int(b) == 8:
        m = "August"
elif int(b) == 9:
        m = "September"
elif int(b) == 10:
        m = "October"
elif int(b) == 11:
     m = "November"
else:
    m = "December"



if x == 0:
    y = "Monday"
elif x == 1:
    y = "Tuesday"
elif x == 2:
    y = "Wednesday"
elif x == 3:
    y = "Thursday"
elif x == 4:
    y = "Friday"
elif x == 5:
    y = "Saturday"
else:
    y = "Sunday"

print(M+ ",you were born on "+y+" "+d+", "+m+" "+a)
