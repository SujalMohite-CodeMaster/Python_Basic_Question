# Write the python program to create a histogram from a given list of integers.

lst = []
char = "$"
for i in range(5):
    lst.append(int(input("enter the values to the list of 5. ")))
    
for i in range(5):
    print(char*lst[i])
