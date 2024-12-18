

import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
playagain=True
while playagain:
    print("")
    playerChoice=input("Enter...\n1 for Rock\n2 for Paper \n3 for Scissors:\n\n")
    #print(type(playerChoice))
    player=int(playerChoice)

    if player<1 or player>3:
        sys.exit("You must enter 1,2,3")

    computerChoice = random.choice("123")

    computer = int(computerChoice)

    print("")
    print("You choose"+str(RPS(player)).replace('RPS.','')+".")
    print("Python choose"+str(RPS(computer)).replace('RPS.','')+".")
    print("")

    if(player == 1 and computer==3):
        print("you win")
    elif(player == 2 and computer==1):
        print("you win")
    elif(player == 3 and computer==2):
        print("you win")
    elif(player == computer):
        print("match tie")
    else :
        print ("python win")
    playagain = input("\nPlay again? \nY for Yes \nQ to Quit\n\n")

    if playagain.lower()=='y':
        continue
    else:
        print("\n")
        print("thank you for playing!\n")
        playagain=False
    sys.exit()














