# Write a python program tha create all possible string using the letteers
# a,e,i,o,u. Ensure that each character is used only once.

lst_of_letters = ['a','e','i','o','u']

import random

random.shuffle(lst_of_letters)
print("".join(lst_of_letters))