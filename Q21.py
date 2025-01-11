# Write the python program to count the number 4 in given list.

lst = [1,2,4,6,4,8,6,23,45,67,3,4,2,5,4,2,4,4]
count = 0
for i in range(len(lst)):
    if lst[i]== 4:
        count += 1
    
print("The count of number 4 in the given list is ",count)