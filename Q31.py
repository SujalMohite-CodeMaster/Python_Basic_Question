# write the python program to find the lcm of two +ve integers.

def lcm(x,y):
    
    if x>y:
        z=x
    else:
        z=y
    
    
    while True:
        if z%x == 0 and z%y ==0:
            lcm = z
            break

        z +=1

    

    return lcm

print(lcm(15,17))
print(lcm(4,6))
print(lcm(336,360))
print(lcm(50,40))