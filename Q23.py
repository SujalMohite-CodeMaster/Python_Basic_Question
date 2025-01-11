# Write the python program to test whether a passed letter is a vowel or not

vowel = input("Enter the letter. ")

lst_vowel = ["A","E","I","O","U"]

for i in range(len(lst_vowel)):
    if vowel.upper() == lst_vowel[i]:
        print(f"The given letter '{vowel}' is vowel.")
        break
else:
    
    print(f"The given letter '{vowel}' is not a vowel.")
