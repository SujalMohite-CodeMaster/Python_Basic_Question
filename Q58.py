#write a python program to convert the distance(in feet) to inches, yards, and miles

input_feet = float(input("Enter the distance in feet. "))

def unit_converter(input_feet):

    inches =input_feet  * 12
    yards = input_feet * 0.333
    miles = input_feet * 0.000189
    return inches,yards,miles

print("The distance in (inches,yard,miles) is ",unit_converter(input_feet))