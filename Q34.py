# Write the python program that return true if the two given integer values are equal 
# or their sum or difference is 5.

def equality_checker(n1,n2):

    if n1 == n2 or n1+n2 == 5 or n1-n2 ==5:
        return True
    else:
        return False
    
print(equality_checker(5,8))
print(equality_checker(10,5))
print(equality_checker(4,4))