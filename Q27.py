"""
Write the python program to print all even numbers from a 
given list of numbers in the same order
and stop printing any after 237 in the sequence
"""
numbers = [386,462,47,418,907,344,236,375,823,566,597
           ,399,162,758,219,918,237,412,566,826,248,86,
           815,67,104,58,512,24,892,894,767,553,81,3,958,743,527]


for i in range(len(numbers)):
    if numbers[i]<=237 and numbers[i]%2 == 0:
        print(numbers[i])
    
