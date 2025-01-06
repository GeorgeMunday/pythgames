import random

def spin(level):
    if level == 1:
        return random.randint(1, 10)
    elif level == 2:
        return random.randint(1, 50)
    elif level == 3:
        return random.randint(1, 100)
    elif level == 4:
        return random.randint(1, 250)
    elif level == 5:
        return random.randint(1, 1000)
    else:
        print("Invalid level!")
        return None
    
def exit_game():
    while True:
        choice = input("Would you like to continue (yes/no)? ").strip().lower()
        if choice == "no":
            print("taking you back to main menu")
            exit()
        elif choice == "yes":
            print("-" * 40)
            main()
        else:
            print("Invalid input, please try again.")

def main():
    while True:
        print("Welcome to the Number Guess Game!!")
        try:
            level = int(input("What level would you like to play (1/2/3/4/5)? \nEnter here:"))
            if level < 1 or level > 5:
                print("Invalid level! Please choose a level between 1 and 5.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
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
                choice1 = int(input("Pick your number: "))
                count += 1
                
                if choice1 == number:
                    print(f"Congrats! You guessed the number {number} in {count} turns!")
                    exit_game()
                elif choice1 < number:
                    print("Pick a higher number.")
                elif choice1 > number:
                    print("Pick a lower number.")
            except ValueError:
                print("invalid input please ty again.")
                
if __name__ == "__main__":
    main()
