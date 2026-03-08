# rock paper scissors
import random
ch = ['rock','paper','scissors']
while True:
    comp = random.choice(ch)
    user = input("enter rock paper or scissors :")
    if user == comp:
        print("it is a tie!")
    elif (user == 'rock' and comp == 'scissors') or (user == 'paper' and comp == 'rock') or (user == 'scissors' and comp == 'paper'):
        print("you win!!")
        print(comp)
    else:
        print("computer wins")
        print(comp)

    c = input("do you want to play again (y/n")
    if c.lower() == 'n':
        break

                  
