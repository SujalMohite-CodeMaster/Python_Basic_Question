"""
Write the python program that returns a string that is n (non-negative integer)
copies of given string.

"""
text = input("enter the string. ")
copy = abs(int(input("Enter the number of copies. ")))

def copy_of_string(text,copy):
    return (text*copy)

print(copy_of_string(text,copy))