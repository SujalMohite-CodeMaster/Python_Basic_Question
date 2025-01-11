"""
Write the python program to get n (non-negative integer) copies of the first 2 character of a given string . 
return n copies of the whole string 
if the length is less than 2.

"""

text = input("Enter the string. ")
n = int(input("Enter the number of copies. "))
def copies(text,n):
    if len(text)<=2:
        return n*text
    else:
        return n*text[0:2]

print("The result is ",copies(text,n))