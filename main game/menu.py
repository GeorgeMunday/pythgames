from time import sleep
from colorama import Fore
import blackjack
import roulette
import slotmachine
import noughtsandcrosses
import numberguess
import rockpaperscissors

def loading():#prints loadingg and pauses for one second every time this function is called so it isnt instant
    print("loading...")
    sleep(1)
    print("-" * 40)

def exit_games():# so they can exit the game , it will stop the program
    print("Thank you for playing, hope to see you soon!")
    exit()

def adult_main():#this the adult main
    print("Welcome to the adults gaming area! We have 3 games on offer.")
    print("To start off, we will give you 100 tokens per game; the goal is to get as many as possible!!")
    #dictionary with all the options in
    options = {
        "1": blackjack.main,
        "2": roulette.main,
        "3": slotmachine.main,
        "4": kid_main,
        "5": exit_games
    }
    
    while True:#choice of what they want to do 
        choice2 = input(Fore.WHITE + "What would you like to play :\n1. = Blackjack \n2. = Roulette\n3. = Slotmachine\n4. = Kids games\n5. = Quit \nEnter here: ")

        if choice2.isnumeric():  # Check if input is numeric
            choice2 = int(choice2)
            if 1 <= choice2 <= 5:
                loading()#loading function
                options[str(choice2)]()  # Call the corresponding game function
                loading()
            else:
                print(Fore.RED + "Invalid choice, please enter a number between 1 and 5.")#diplayed if invalid input
        else:
            print(Fore.RED + "Invalid input, please enter a valid number.")

def kid_main():#this is the kids menu 
    print("Welcome to the kids gaming area! We have 3 games that you can play.")
    
    options = {
        "1": noughtsandcrosses.main,
        "2": numberguess.main,
        "3": rockpaperscissors.main,
        "4": exit_games
    }
    
    while True:
        choice3 = input(Fore.WHITE + "What would you like to play :\n1. = Noughts and Crosses \n2. = Number Guessing\n3. = Rock Paper Scissors\n4. = Quit \nEnter here: ")
        
        if choice3.isnumeric():  # Check if input is numeric
            choice3 = int(choice3)
            if 1 <= choice3 <= 5:
                loading()
                options[str(choice3)]()  # Call the corresponding game function
                loading()
            else:
                print(Fore.RED + "Invalid choice, please enter a number between 1 and 5.")
        else:
            print(Fore.RED + "Invalid input, please enter a valid number.")

def main():
    while True:
        print(Fore.WHITE + "Welcome to Python games")
        choice1 = input("What is your age?\nEnter here: ")
        
        if choice1.isnumeric():  # Check if input is numeric
            choice1 = int(choice1)
            if choice1 > 17:
                loading()
                adult_main()
            elif 0 < choice1 < 17:
                loading()
                kid_main()
            else:
                print(Fore.RED + "Invalid input, age must be a positive number.")
        else:
            print(Fore.RED + "Invalid input, please enter a valid number.")

if __name__ == "__main__":
    main()