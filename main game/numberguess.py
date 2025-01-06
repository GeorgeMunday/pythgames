import random
from colorama import Fore
def spin(level):
    ranges = {1: 10, 2: 50, 3: 100, 4: 250, 5: 1000}
    if level not in ranges:
        print("Invalid level!")
        return None
    return random.randint(1, ranges[level]) 
    
def exit_game():
    while True:
        choice = input(Fore.WHITE + "Would you like to continue (yes/no)? ").strip().lower()
        if choice == "no":
            print("taking you back to main menu")
            exit()
        elif choice == "yes":
            print("-" * 40)
            main()
        else:
            print(Fore.RED + "Invalid input, please try again.")

def main():
    while True:
        print(Fore.WHITE + "Welcome to the Number Guess Game!!")
        try:
            level = int(input("What level would you like to play (1/2/3/4/5)? \nEnter here:"))
            if level < 1 or level > 5:
                print(Fore.RED + "Invalid level! Please choose a level between 1 and 5.")
                continue
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 5.")
            continue
        
        number = spin(level)
        if number is None:
            return
        
        options = {
            1: "Pick a number between 1 and 10",
            2: "Pick a number between 1 and 50",
            3: "Pick a number between 1 and 100",
            4: "Pick a number between 1 and 250",
            5: "Pick a number between 1 and 1000"
        }
        print(options[level])
        
        count = 0
        while True:
            try:
                choice1 = int(input(Fore.WHITE + "Pick your number: "))
                count += 1

                if choice1 == number:
                    print(f"Congrats! You guessed the number {number} in {count} turns!")
                    exit_game()
                elif choice1 < number:
                    print("Pick a higher number.")
                elif choice1 > number:
                    print("Pick a lower number.")
            except ValueError:
                print(Fore.RED + "invalid input please try again.")
                
if __name__ == "__main__":
    main()
