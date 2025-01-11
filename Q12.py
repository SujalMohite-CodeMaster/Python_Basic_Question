# write a python program to prints the calender for given month and year 
# note use calender module.

import calendar

year = int(input("Enter the year :"))
month = int(input("Enter the month :"))

print(calendar.month(year,month))