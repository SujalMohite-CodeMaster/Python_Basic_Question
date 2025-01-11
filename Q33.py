# Write the python program to sum of two given integers,
# However, if the sum is between 15 and 20 it will return 20.

n1 = int(input("Enter the 1st number. "))
n2 = int(input("Enter the 2nd number. "))

sum = n1 + n2

if sum >= 15 and sum <=20 :
    print("The sum is 20")
else:
    print("The sum is ",sum)