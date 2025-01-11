# write the python program to calculate the difference between the given numbers and 17. if the number is greater than 17, return twice of the absolute difference.
number = int(input("Enter the number. "))

if number >17:
    result = (number-17)
    print(abs(result*2))
else:
    print(abs(number-17))