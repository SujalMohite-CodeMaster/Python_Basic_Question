# Write the python program to print the sum of three given numbers. if the values are equals return three times their sum.

def sum(n1,n2,n3):
    if n1==n2==n3:
        return (n1+n2+n3)*3
    else:
        return n1+n2+n3
    
n1 = float(input("Enter the 1st number."))
n2 = float(input("Enter the 2st number."))
n3 = float(input("Enter the 3st number."))

print(sum(n1,n2,n3))