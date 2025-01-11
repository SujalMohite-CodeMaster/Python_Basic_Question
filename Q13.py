# Write a python program to calculate the number of days between two dates.
from datetime import date


f_date = date(2025,5,31)
l_date = date(2026,5,31)
delta = l_date - f_date

print(delta.days)