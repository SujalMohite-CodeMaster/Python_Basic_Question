import random
n=int(input("Enter the length of password :-"))
name = str(input("Enter the name for making password : "))

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numeric = "1234567890"
symbol = "!@#$%^&*?"



password = random.choice(uppercase + lowercase + numeric + symbol)

while(len(password)!=n):
  password = password + random.choice(uppercase + lowercase + numeric + symbol)

name=name.replace("a","@")
name=name.replace("s","$")
new_password = name + password

length = len(new_password)-len(name)

print(new_password[0:length])