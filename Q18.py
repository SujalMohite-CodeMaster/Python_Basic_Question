# Write the python program to get a newly generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begin with "Is".

def new_string(string):

    if len(string)>=2 and string[:2]== "Is":
        return string
    else:
        return "Is"+string
print(new_string("Sujal"))
print(new_string("Isdigit"))
