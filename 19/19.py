import sys
import os

sys.path.append(os.path.abspath('../scripts'))

import functions

def numdays(month, year):
    list30 = ['September','April','June','November']
    list31 = ['January','March','May','July','August','October','December']
    listother = ['February']
    if month in list30:
        return(30)
    elif month in list31:
        return(31)
    elif month in listother:
        if year % 4 > 0:
            return(28)
        elif year % 4 == 0 and year % 400 == 0:
            return(29)
        else:
            return(28)

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# day 1 = monday, day 7 = Sundays
normalyear = [31, 28, 31, 30, 31, 30, 31, 31, 30 , 31, 30, 31]
leapyear = normalyear.insert(1,29)

normalYearFirstDay = []
runningtotal = 0

for days in normalyear:
    runningtotal += days
    normalYearFirstDay.append(runningtotal)

print(normalYearFirstDay)

def numSquare(num):
    return num**2

maxNum = max(1,2,3, key=numSquare)

print(maxNum)
