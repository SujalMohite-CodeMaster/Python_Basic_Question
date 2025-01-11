# Write the python program to calculate the distance between the points (x1,y1) and (x2,y2).

from math import sqrt
x1 = float(input("Enter the x1 value. "))
y1 = float(input("Enter the y1 value. "))
x2 = float(input("Enter the x2 value. "))
y2 = float(input("Enter the y2 value. "))

distance = sqrt((x2-x1)**2 + (y2-y1)**2)

print("The distane between the given points is ",distance)