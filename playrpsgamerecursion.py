from enum import Enum
import random
import sys

def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0
    def play_rps():
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3
        playerChoice=input(f"{name} Enter...\n1 for Rock\n2 for Paper \n3 for Scissors:\n\n")
        #print(type(playerChoice))
        player=int(playerChoice)

        if playerChoice  not in ["1","2","3"]:
            print(f"{name} must enter 1,2,3")
            return play_rps()
            

        computerChoice = random.choice("123")

        computer = int(computerChoice)

        print("")
        print(f"{name} choose {str(RPS(player)).replace('RPS.','').title()}.")
        print(f"Python choose {str(RPS(computer)).replace('RPS.','').title()}.")
        print("")
        def game_play(player,computer):
            nonlocal player_wins
            nonlocal python_wins
            if(player == 1 and computer==3):
                player_wins+=1
                print(f"{name} win")
            elif(player == 2 and computer==1):
                player_wins+=1
                print(f"{name} win")
            elif(player == 3 and computer==2):
                player_wins+=1
                print(f"{name} win")
            elif(player == computer):
            
                print("match tie")
            else :
                python_wins+=1
                print ("python win")
        
        game_result = game_play(player,computer)
        print(game_result)

        nonlocal game_count

        game_count+=1
        print(f"\nGame count: {str(game_count)}")
        print(f"\n{name} wins: {str(player_wins)}")
        print(f"\nPython wins: {str(python_wins)}")
        playagain = input("\nPlay again? \nY for Yes \nQ to Quit\n\n")

        if playagain.lower()=='y':
            return play_rps()
        else:
            print("\n")
            print("thank you for playing!\n")
            sys.exit("bye")
    return play_rps

#play=rps()
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game"
    )
    parser.add_argument(
        "-n","--name",metavar="name",required=True,help="The name of the person"
    )
    args = parser.parse_args()
    rock_paper_scissors =rps(args.name)
    rock_paper_scissors()
    #play()