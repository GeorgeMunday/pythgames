import random  # Import the random module to generate random numbers

def bank_balance(bank, bet_amount, result, choice):
    # Update the bank balance based on the result of the bet
    if result == "win":
        # Update the bank balance based on the bet type
        if choice in [1, 2, 3]:  # Odd/Even, Red/Black, High/Low
            bank += bet_amount
        elif choice == 4:  # Specific number
            bank += bet_amount * 35  # 35 times the bet amount for a specific number win
    else:
        bank -= bet_amount  # Subtract the bet amount if the player loses
    return bank  # Return the updated bank balance

def place_bet(choice, money):
    # Define the betting options for each choice
    options = {
        1: ["odd", "even"],  # Odd or Even
        2: ["red", "black"],  # Red or Black
        3: ["high", "low"],   # High or Low
        4: "a number between 0 and 36",  # Specific number
    }
    
    while True:
        try:
            # Ask the player how many tokens they want to bet
            bet_amount = int(input(f"You have {money} tokens. How many tokens would you like to bet? "))
            if bet_amount > money:  # Check if the player has enough tokens
                print("You do not have enough tokens.")
                break  # Exit the loop if the player doesn't have enough tokens
            if bet_amount <= 0:  # Bet must be greater than 0
                print("Bet amount must be greater than 0.")
                continue  # Ask for a new bet if the amount is invalid
            
            print(f"You have bet {bet_amount} tokens.")
            print(f"Option: {options.get(choice, 'Invalid choice')}")
            
            # Get the player's choice for the bet
            if choice in [1, 2, 3]:
                bet_choice = input(f"Enter your choice ({'/'.join(options[choice])}): ").lower().strip()
                if bet_choice in options[choice]:
                    return bet_amount, bet_choice  # Return bet amount and choice
            elif choice == 4:
                bet_choice = int(input("Enter your number (0-36): "))
                if 0 <= bet_choice <= 36:  # Ensure the number is within the valid range
                    return bet_amount, bet_choice  # Return bet amount and number
    
            print("Invalid choice. Please try again.")  # If the player enters an invalid choice
        except ValueError:
            print("Invalid input. Please enter a number.")  # Handle non-integer input

def spin_wheel():
    # Simulate spinning the roulette wheel
    number = random.randint(0, 36)  # Random number between 0 and 36
    color = random.choice(["red", "black"])  # Randomly select red or black
    odd_even = "odd" if number % 2 != 0 else "even"  # Determine if the number is odd or even
    high_low = "high" if 19 <= number <= 36 else "low" if 1 <= number <= 18 else "zero"  # Determine if the number is high, low, or zero
    return number, color, odd_even, high_low  # Return the results of the spin

def main():
    money = 100  # Initial bank balance (100 tokens)
    print("Welcome to the Roulette Game!")  # Display a welcome message
    
    while True:
        # Display the available betting options
        print("\nWhat would you like to bet on?")
        print("1. Odd or Even")
        print("2. Red or Black")
        print("3. High or Low")
        print("4. Specific Number")
        print("5. Quit")
        
        choice = input("Enter your choice: ")  # Get the player's choice
        
        # If the player chooses to quit
        if choice == "5":
            print("Thanks for playing! Goodbye!")  # Display a goodbye message
            break  # Exit the game loop
        
        # Validate the player's input for valid betting options
        if not choice.isnumeric() or int(choice) not in [1, 2, 3, 4]:
            print("Invalid choice. Please try again.")  # If the choice is invalid
            continue  # Prompt the player again
        
        choice = int(choice)  # Convert the choice to an integer
        bet_amount, bet_choice = place_bet(choice, money)  # Call place_bet function to get the bet details
        
        # Spin the roulette wheel and get the results
        number, color, odd_even, high_low = spin_wheel()
        print(f"\nThe wheel spins... The ball lands on {number} ({color}).")
        print(f"Odd/Even: {odd_even}, High/Low: {high_low}")
        
        # Determine the result of the spin
        result_spin = {
            1: odd_even,  # Odd/Even bet
            2: color,  # Red/Black bet
            3: high_low,  # High/Low bet
            4: number,  # Specific number bet
        }
        
        # Check if the player won or lost based on their bet choice
        if bet_choice == result_spin[choice]:
            print("Congratulations, you win!")  # Player wins
            result = "win"
        else:
            print("Sorry, you lose.")  # Player loses
            result = "lose"
        
        # Update the player's bank balance after the bet
        money = bank_balance(money, bet_amount, result, choice)
        print(f"Your new balance is: {money} tokens.")
        
        # If the player runs out of money, end the game
        if money <= 0:
            print("You are out of money! Game over.")
            break  # End the game

# Run the main function if this script is executed
if __name__ == "__main__":
    main()  # Start the game
