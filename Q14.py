# write the python program to print volume of sphere
import math
radius = float(input("enter the radius (if radius is not known then enter 0)"))
diameter = float(input("enter the diameter (if diameter is not known then enter 0)"))

if radius != "0":
    volume = 4/3 * math.pi * (radius**3)
    print(f"The Volume of sphere with radius {radius} is {volume}")
else:
    volume = math.pi * ((diameter**3)/6)
    print(f"The Volume of sphere with Diameter {diameter} is {volume}")



