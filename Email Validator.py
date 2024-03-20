# Email essentials : (i) a-z, (ii) 0-9, (iii) . _ anyone single time before @
#                    (iv) . 2ns or 3rd positions

import re  # RegEx module

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"  
# '^' --> this checks the first character, 
# '\' --> this checks the total count of particular character, 
# '?' --> this works in binary way(true for 1 and any other value as false), 
# '\w' --> this searches for particular character in a string, 
# '{}' --> this finds position of a particular character 

user_email = input("Enter your Email : ")

if re.search(email_condition,user_email):
    print("Right email!!")
else:
    print("Wrong email!!")