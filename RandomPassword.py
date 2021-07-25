import random
import string

print("Welcome to password generator")

length = int(input('\n Enter the password lenghth'))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#combines all the characters

all = lower + upper + num  + symbols

temp = random.sample(all, length)

password =  "".join(temp)

print(password)