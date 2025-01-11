"""
Write the python program that determins whether given number (accept from the user )
is even or odd and print an appropriate message to the user.
"""

number = int(input("Enter any number to check even or odd. "))

def checker(number):
    if number%2 == 0 :
        return "Even"
    else:
        return "Odd"
    
print(f"The given number {number} is an {checker(number)} number.")