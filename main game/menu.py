from time import sleep
from colorama import Fore
import blackjack
import roulette
import slotmachine
import noughtsandcrosses
import numberguess
import rockpaperscissors

def loading():  # Prints "loading..." and pauses for one second each time it's called, to avoid the process being instant
    print("loading...")
    sleep(1)  # Pause for 1 second
    print("-" * 40)  # Print a separator line

def exit_games():  # This function is used to exit the game, it stops the program
    print("Thank you for playing, hope to see you soon!")  # Message displayed when exiting
    exit()  # Terminates the program

def adult_main():  # The main menu for the adult games
    print("Welcome to the adults gaming area! We have 3 games on offer.")  # Welcome message for adult area
    print("To start off, we will give you 100 tokens per game; the goal is to get as many as possible!!")  # Information on tokens
    # A dictionary with game options, mapped to their corresponding functions
    options = {
        "1": blackjack.main,  # Option 1: Blackjack
        "2": roulette.main,  # Option 2: Roulette
        "3": slotmachine.main,  # Option 3: Slot Machine
        "4": kid_main,  # Option 4: Switch to kids games
        "5": exit_games  # Option 5: Exit the game
    }
    
    while True:  # Continuously prompt user for their choice
        choice2 = input(Fore.WHITE + "What would you like to play :\n1. = Blackjack \n2. = Roulette\n3. = Slotmachine\n4. = Kids games\n5. = Quit \nEnter here: ")

        if choice2.isnumeric():  # Check if the input is a valid number
            choice2 = int(choice2)  # Convert input to integer
            if 1 <= choice2 <= 5:  # Validate the input is within the correct range
                loading()  # Call the loading function before starting the game
                options[str(choice2)]()  # Call the selected game function
                loading()  # Call loading after each game
            else:
                print(Fore.RED + "Invalid choice, please enter a number between 1 and 5.")  # Error message for invalid choice
        else:
            print(Fore.RED + "Invalid input, please enter a valid number.")  # Error message for non-numeric input

def kid_main():  # The main menu for the kids games
    print("Welcome to the kids gaming area! We have 3 games that you can play.")  # Welcome message for kids games
    
    options = {
        "1": noughtsandcrosses.main,  # Option 1: Noughts and Crosses (Tic-Tac-Toe)
        "2": numberguess.main,  # Option 2: Number Guessing Game
        "3": rockpaperscissors.main,  # Option 3: Rock, Paper, Scissors
        "4": exit_games  # Option 4: Exit the game
    }
    
    while True:  # Continuously prompt user for their choice
        choice3 = input(Fore.WHITE + "What would you like to play :\n1. = Noughts and Crosses \n2. = Number Guessing\n3. = Rock Paper Scissors\n4. = Quit \nEnter here: ")
        
        if choice3.isnumeric():  # Check if the input is a valid number
            choice3 = int(choice3)  # Convert input to integer
            if 1 <= choice3 <= 4:  # Validate the input is within the correct range
                loading()  # Call loading function before starting the game
                options[str(choice3)]()  # Call the selected game function
                loading()  # Call loading after each game
            else:
                print(Fore.RED + "Invalid choice, please enter a number between 1 and 4.")  # Error message for invalid choice
        else:
            print(Fore.RED + "Invalid input, please enter a valid number.")  # Error message for non-numeric input

def main():  # The main entry point of the program
    while True:  # Continuously prompt for user input
        print(Fore.WHITE + "Welcome to Python games")  # Welcome message
        choice1 = input("What is your age?\nEnter here: ")  # Ask the user for their age
        
        if choice1.isnumeric():  # Check if the input is numeric
            choice1 = int(choice1)  # Convert input to integer
            if choice1 > 17:  # If the user is an adult
                loading()  # Call loading before starting adult games
                adult_main()  # Call the adult games menu
            elif 0 < choice1 < 17:  # If the user is a kid (under 17)
                loading()  # Call loading before starting kids games
                kid_main()  # Call the kids games menu
            else:
                print(Fore.RED + "Invalid input, age must be a positive number.")  # Error message for invalid age
        else:
            print(Fore.RED + "Invalid input, please enter a valid number.")  # Error message for non-numeric input

if __name__ == "__main__":  # Ensure the script runs if this is the main program
    main()  # Call the main function to start the program
