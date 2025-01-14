# write a python program to sum the first n positive integers.

n = int(input("Enter the value of n. "))

def sum_of_n_positive(n):

    sum = (n*(n+1))/2
    return sum

print("Sum of first ",n,"positive integers is :",sum_of_n_positive(n))

### In more logical way

result = sum(range(n+1))
print(result)