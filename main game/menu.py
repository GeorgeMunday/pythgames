from time import sleep
from colorama import Fore
import blackjack
import roulette
import slotmachine
import noughtsandcrosses
import numberguess
import rockpaperscissors
 

def loading():
    print("loading...")
    sleep(1)
    print("-" * 40)
    
def exit_games():
    print("thank you for playing hope to see you soon")
    exit()
    
def adult_main():
    choice2 = 0
    print("Welcome to the adults gaming area! We have 3 games on offer.")
    print("To start off, we will give you 100 tokens per game the goal is to get as many as posible !!.")
    options = {
        "1": blackjack.main,
        "2": roulette.main,
        "3": slotmachine.main,
        "4": kid_main,
        "5": exit_games
        }
    while choice2 < 5 :
        choice2 = input(Fore.WHITE + "What would you like to play :\n1. = Blackjack \n2. = Roulette\n3. = Slotmachine\n4. = Kids games\n5. = Quit \nEnter here")
        if choice2.isnumeric:
           choice2 = int(choice2)
           loading()
           options[str(choice2)]()
           loading()
        else:
            print(Fore.RED + "invalid inout")
        
def kid_main():
    choice3 = ""
    print("Welcome to the kids gaming area! We have 3 games that you can play.")
    options = {
        "1": noughtsandcrosses.main,
        "2": roulette.main,
        "3": slotmachine.main,
        "4": kid_main,
        "5": exit_games
    }
    while True:
        choice3 = input(Fore.WHITE + "What would you like to play:\n1. = noughtsandcrosses\n2. = guess the number\n3. = rock paper scissors\nEnter here: ")
        if choice3.isnumeric():
            choice3 = int(choice3)
            if choice3 == 1:
                loading()
                # Call the noughtsandcrosses game function
            elif choice3 == 2:
                loading()
                # Call the guess the number game function
            elif choice3 == 3:
                loading()
                # Call the rock paper scissors game function
            else:
                print(Fore.RED + "Invalid input")
        else:
            print(Fore.RED + "Invalid input")
            
def main():
    while True:
        print(Fore.WHITE + "Welcome to Python games")
        choice1 = input("What is your age?\nEnter here: ")
        if choice1.isnumeric():
            choice1 = int(choice1)
            if choice1 > 17:
                loading()
                adult_main()
            elif 0 < choice1 < 17:
                loading()
                kid_main()
            else:
                print(Fore.RED + "Invalid input")
        else:
            print(Fore.RED + "Invalid")
if __name__ == "__main__":
    main()