# write the python program to sum three given integer. however if two values 
# are equal, the sum will be zero.

n1 = int(input("Enter the 1st number. "))
n2 = int(input("Enter the 2nd number. "))
n3 = int(input("Enter the 3rd number. "))

def checker(x,y,z):

    if x == y or x==z:
        return 0
    elif y == x or y == z:
        return 0
    elif z == x or z == y:
        return 0
    else:
        return x+y+z

print("The sum of given integers is ",checker(n1,n2,n3))
