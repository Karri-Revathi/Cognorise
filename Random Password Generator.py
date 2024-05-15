import random
import string

char=string.ascii_letters
char+=string.digits
char+=string.punctuation

length=int(input(print("Enter length of the password:")))

password=""

if(length<=16):
  for i in range(length):
    password+=random.choice(char)
  print("Your random strong password is:",password)
else:
  print("Length of the password must be less than 16")
