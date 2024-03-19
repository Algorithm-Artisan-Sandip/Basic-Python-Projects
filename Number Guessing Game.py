import random
print("Enter the range of number you want to guess : ")
lower = int(input("Enter the lower bound : "))
upper = int(input("Enter the upper bound : "))
target = random.randint(lower,upper)
while True :
    userChoice = input("Guess the target or quit : ")
    if(userChoice=="quit"):
        print("Quitting!!")
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Correct guess, Congratulations!!!")
        break
    elif(userChoice<target):
        print("OOPS!!! Guess bigger number...")
    elif(userChoice>target):
        print("OOPS!!! Guess smaller number...")

print("----- Game Over -----")