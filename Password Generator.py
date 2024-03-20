import random
import string

charValues = string.ascii_letters + string.digits + string.punctuation
num = int(input("Enter number of characters you want in your password : "))

#! list comprehension syntax
password = "".join([random.choice(charValues) for i in range(0,num)])

#! Alternate way : 
# password = ""
# for i in range(0,num):
#     password+=random.choice(charValues)

print("Suggested password :",password)