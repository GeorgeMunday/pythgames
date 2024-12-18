from time import sleep
from colorama import Fore
import blackjack
import roulette
import slotmachine

def loading():
    print("loading...")
    sleep(1)
    print("-" * 40)
    
def exit_games():
    print("thank you for playing hope to see you soon")
    exit()
    
def adult_main():
    choice2 = ""
    print("Welcome to the adults gaming area! We have 3 games on offer.")
    print("To start off, we will give you 100 tokens per game the goal is to get as many as posible !!.")
    while True:
        choice2 = input(Fore.WHITE + "What would you like to play :\n1. = Blackjack\n2. = Roulette\n3. = Slotmachine\n4. = Kids games\n5. = Quit \nEnter here:")
        if choice2.isnumeric():
            choice2 = int(choice2)
            if choice2 == 1:
                loading()
                blackjack.main()
                loading()
            elif choice2 == 2:
                loading()
                roulette.main()
                loading()
            elif choice2 == 3:
                loading()
                slotmachine.main()
                loading()
            elif choice2 == 4 :
                loading()
                kid_main()
            elif choice2 == 5 :
                loading()
                exit_games()
            else:
                print(Fore.RED + "Invalid input")
        else:
            print(Fore.RED + "invalid input")
    
def kid_main():
    choice3 = ""
    print("Welcome to the kids gaming area! We have 3 games that you can play.")
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