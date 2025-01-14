# Write a python program to get the execution time of python method.

# Import time modue to work with time related functions

import time
def sum_of_n_numbers(n):
    start_time = time.time()
    sum = 0
    for i in range(1,n+1):
        sum += i
    end_time = time.time()

    return sum , start_time,end_time
n =5 
print(f"The sum of 1 0 to {n} and required to calculate is {sum_of_n_numbers(n)}")