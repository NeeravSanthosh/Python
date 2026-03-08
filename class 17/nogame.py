# number
import random
comp = random.randint(1,10)
while True:
    user = int(input("enter the number 1 - 10"))
    if user == comp:
        print("you got it!!")
        break
    else:
        print("try again")
