import random
from colorama import Fore

# Function to randomly select a number based on the chosen difficulty level
def spin(level):
    # Defines the maximum range for each level
    ranges = {1: 10, 2: 50, 3: 100, 4: 250, 5: 1000}
    
    # Check if the level is valid (within the defined levels)
    if level not in ranges:
        print("Invalid level!")
        return None  # Return None if the level is invalid
    return (random.randint(1, ranges[level]), ranges[level])  # Return a random number and the max range for the level

# Function to handle input validation for number ranges
def rangechecker(message, min, max):
    while True:
        try:
            # Prompt user for input and convert it to an integer
            num = int(input(Fore.WHITE + message).strip().lower())
            
            # Check if the number is within the valid range
            if num < min or num > max:
                print(Fore.RED + f"Invalid input! Please enter a number between {min} and {max}.")
            else:
                return num  # Return the valid number
        except:
            # Handle non-integer inputs and inform the user
            print(Fore.RED + "Invalid input, please try again.")

# Function to ask user if they want to continue or exit the game
def exit_game():
    while True:
        # Prompt user to continue or exit
        choice = input(Fore.WHITE + "Would you like to continue (yes/no)? ").strip().lower()
        if choice == "no":
            print("Taking you back to main menu")  # Exit the game
            return ""  # Return an empty string to indicate exit
        elif choice == "yes":
            print("-" * 40)  # Separator for a clean break
            main()  # Restart the game by calling the main function
        else:
            # Handle invalid input
            print(Fore.RED + "Invalid input, please try again.")

# Main function to run the game
def main():
    list1 = []  # List to store previously guessed numbers
    while True:
        print(Fore.WHITE + "Welcome to the Number Guess Game!!")
        
        # Prompt user to select the difficulty level
        level = rangechecker("What level would you like to play (1/2/3/4/5)? \nEnter here:", 1, 5)
        
        # Call spin() to generate a random number and get the max range for the level
        number = spin(level)
        maxrange = number[1]  # Max range for the chosen level
        number = number[0]  # The randomly selected number
        
        if number is None:
            return  # Exit if the number is None (invalid level)
        
        # Dictionary containing the prompts for each level
        options = {
            1: "Pick a number between 1 and 10",
            2: "Pick a number between 1 and 50",
            3: "Pick a number between 1 and 100",
            4: "Pick a number between 1 and 250",
            5: "Pick a number between 1 and 1000"
        }
        print(options[level])  # Display the prompt based on the chosen level
        
        count = 1  # Initialize the number of attempts
        while True:
            # Prompt user to input their guess
            choice1 = rangechecker("Pick your number: ", 1, maxrange)
            
            # Check if the guess is correct
            if choice1 == number:
                print(f"Congrats! You guessed the number {number} in {count} turns!")
                exit_game()  # Ask the user if they want to continue or exit
                return ""  # Exit the game if guessed correctly
            elif choice1 in list1:
                # If the number was already guessed, prompt again
                print("You've already selected this number.")
                continue
            elif choice1 < number:
                # If the guess is too low, prompt for a higher number
                print("Pick a higher number.")
            else:
                # If the guess is too high, prompt for a lower number
                print("Pick a lower number.")
            
            list1.append(choice1)  # Add the guess to the list of guessed numbers
            count += 1  # Increment the attempt counter


if __name__ == "__main__":
    main()
