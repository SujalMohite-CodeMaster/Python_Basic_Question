# Write a python program that accept a sequence of comma-separated numbers from the user and generate the list and tuple of those numbers.

number = input("Enter the sequence of number separated by commas. ")

lst = number.split(",")

print("List: ",list(lst))
print("Tuple: ",tuple(lst))