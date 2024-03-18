from time import *
import random as r
def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error+=1
        except Exception as e:
            error+=1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

while True:
    choice = input("Ready to enter (yes/no) :")
    if choice=="no":
        print("Thank You!!!")
        break
    elif choice=="yes":
        
        test = ["A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea",
        "my name is Sandip Pramanik", "welcome to my project"]
        test1 = r.choice(test)
        print("*****typing speed*****")
        print(test1)
        print()
        print()
        time_1 = time()
        testinput = input("Enter : ")
        time_2 = time()
        print('Speed : ',speed_time(time_1,time_2,testinput)*60,"WPM")
        print("Error : ",mistake(test1,testinput))
    else:
        print("Invalid input")
        print("Thank You!!!")
        break