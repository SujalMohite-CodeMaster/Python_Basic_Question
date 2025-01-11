#Write the python program to test whether a number is within 100 of 1000 or 2000

number = int(input("Enter the number. "))

diff = 1000 -number

if diff <= 100 :
    print(True)
else:
    print(False)