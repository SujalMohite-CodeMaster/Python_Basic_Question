"""
Write the python program that check whether a specified value is cotained
within a group of values.
"""

grp_of_numbers = ['1','4','3','3','7','8']

value = input("Enter the value. ")

def value_in_grp(value):
    return value in grp_of_numbers

print(value_in_grp(value))