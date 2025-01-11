# Write the python program to add two object if both objects are integers.

def add(n1,n2):
    if not (isinstance(n1,int) and isinstance(n2,int)):
        return "Input must be integres."
    else:
        return n1 +n2

print(add(5,8))
print(add(5,8.4))