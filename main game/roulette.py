import random

def bank_balance(choice, result):
    bank = 100  # Initial bank balance
    if result == "win":
        # If the player wins, the bank increases based on the bet type
        if choice in [1, 2, 3]:  # Odd/Even, Red/Black, High/Low
            bank *= 2
        elif choice == 4:  # Specific number
            bank *= 36
    return bank

def place_bet(choice, money):
    answer = ["odd", "even"]
    answer1 = ["red", "black"]
    answer2 = ["high", "low"]
    options = {
        1: "pick odd or even",
        2: "pick red or black",
        3: "pick high or low",
        4: "pick a number between 0 and 36",
    }
    
    while True:
        # Ask the player how many tokens they want to bet
        choice1 = int(input(f"You have {money} tokens. How many tokens would you like to bet? "))
        if choice1 > money:
            print("You do not have enough tokens.")
            continue
        else:
            print(f"You have bet {choice1} tokens.")
            print(options.get(choice, "Invalid choice"))
            # Get the player's choice for the bet
            choice2 = input("Enter your choice: ").lower().strip()

            # Validate the player's bet based on the chosen option
            if choice == 1 and choice2 in answer:
                return choice2
            elif choice == 2 and choice2 in answer1:
                return choice2
            elif choice == 3 and choice2 in answer2:
                return choice2
            elif choice == 4 and choice2.isnumeric() and 0 <= int(choice2) <= 36:
                return int(choice2)

def result(choice):
    # Simulate a spin of the roulette wheel
    number = random.randint(0, 36)
    color = random.choice(["red", "black"])
    odd_even = "odd" if number % 2 != 0 else "even"
    high_low = "high" if 19 <= number <= 36 else "low" if 1 <= number <= 18 else "zero"
    options = {
        1: odd_even,
        2: color,
        3: high_low,
        4: number,
    }
    return options.get(choice, "Invalid choice")

def main():
    while True:
        # Ask the player what they want to bet on
        choice = input(
            "What would you like to bet on? \n"
            "1. Odd or Even \n"
            "2. Red or Black \n"
            "3. High or Low \n"
            "4. Specific Number \n"
            "5. Quit \n"
            "Enter your choice: ")
        
        if choice == "5":
            print("Taking you back to the main menu.")
            break
        
        if not choice.isnumeric() or int(choice) not in [1, 2, 3, 4]:
            print("Invalid choice.")
            continue
        
        choice = int(choice)
        
        # Get the result of the roulette spin
        result_spin = result(choice)
        # Get the player's bet and current money
        money = 100  # Starting money
        player_choice = place_bet(choice, money)
        print(f"The result is: {result_spin}")
        
        # Check if the player wins or loses
        if player_choice == result_spin:
            print("You win!")
            game_result = "win"
        else:
            print("You lose.")
            game_result = "lose"
        
        # Update balance after the result
        money = bank_balance(choice, game_result)
        print(f"Your balance is now: {money}")

# Run the game
if __name__ == "__main__":
    main()
