# write a python that accept a filename from the user and print the extension of the file

filename = input("Enter the file name. ")

f_exte = filename.split(".")

print("The extension of the given file is "+ repr(f_exte))