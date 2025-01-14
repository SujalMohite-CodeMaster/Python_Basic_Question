# Write a python program to convert height (in feet and inches) to centimeters.

feet = float(input("Enter the height in feet. "))

def feet_to_centimeter(feet):
    result_feet = feet * 30
    result_inch = feet * 12

    return result_feet,result_inch

print(f"The height in (centimeter , inche) is {feet_to_centimeter(feet)}")