# write a python function that takes a sequence of numbers and determine 
# whether all the numbers are different from each other.

lst = []

for i in range(1,11):
    lst.append(i)

def test_distinct(lst):
    if len(lst) == len(set(lst)):
        return True
    else:
        return False

print(test_distinct(lst))
lst.append(4)
print(test_distinct(lst))

