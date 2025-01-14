# Write a python program to parse a string to float or integer.

def test (string):
    try:
        return int(string)
    except ValueError:
        return float(string)
    
print(test("34"))
print(test("46.25"))