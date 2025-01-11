# Write the python program that computes the
# greatest common divisor (GCD) of two positive integers.

def gcd(x,y):
    gcd = 1
    if x%y ==0:
        return y
    
    for i in range(int(y/2),0,-1):
        if x%i == 0 and y%i ==0:
            gcd = i
            break

    return gcd

print(gcd(12,17))
print(gcd(4,6))
print(gcd(336,360))
print(gcd(50,40))