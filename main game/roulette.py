import random

def bank_balance(bank, bet_amount, result, choice):
    if result == "win":
        # Update the bank balance based on the bet type
        if choice in [1, 2, 3]:  # Odd/Even, Red/Black, High/Low
            bank += bet_amount
        elif choice == 4:  # Specific number
            bank += bet_amount * 35
    else:
        bank -= bet_amount
    return bank

def place_bet(choice, money):
    options = {
        1: ["odd", "even"],
        2: ["red", "black"],
        3: ["high", "low"],
        4: "a number between 0 and 36",
    }
    
    while True:
        try:
            # Ask the player how many tokens they want to bet
            bet_amount = int(input(f"You have {money} tokens. How many tokens would you like to bet? "))
            if bet_amount > money:
                print("You do not have enough tokens.")
                break
            if bet_amount <= 0:
                print("Bet amount must be greater than 0.")
                continue
            
            print(f"You have bet {bet_amount} tokens.")
            print(f"Option: {options.get(choice, 'Invalid choice')}")
            
            # Get the player's choice for the bet
            if choice in [1, 2, 3]:
                bet_choice = input(f"Enter your choice ({'/'.join(options[choice])}): ").lower().strip()
                if bet_choice in options[choice]:
                    return bet_amount, bet_choice
            elif choice == 4:
                bet_choice = int(input("Enter your number (0-36): "))
                if 0 <= bet_choice <= 36:
                    return bet_amount, bet_choice
            
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def spin_wheel():
    number = random.randint(0, 36)
    color = random.choice(["red", "black"])
    odd_even = "odd" if number % 2 != 0 else "even"
    high_low = "high" if 19 <= number <= 36 else "low" if 1 <= number <= 18 else "zero"
    return number, color, odd_even, high_low

def main():
    money = 100  # Initial bank balance
    print("Welcome to the Roulette Game!")
    
    while True:
        print("\nWhat would you like to bet on?")
        print("1. Odd or Even")
        print("2. Red or Black")
        print("3. High or Low")
        print("4. Specific Number")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        if choice == "5":
            print("Thanks for playing! Goodbye!")
            break
        
        if not choice.isnumeric() or int(choice) not in [1, 2, 3, 4]:
            print("Invalid choice. Please try again.")
            continue
        
        choice = int(choice)
        bet_amount, bet_choice = place_bet(choice, money)
        
        # Spin the roulette wheel
        number, color, odd_even, high_low = spin_wheel()
        print(f"\nThe wheel spins... The ball lands on {number} ({color}).")
        print(f"Odd/Even: {odd_even}, High/Low: {high_low}")
        
        # Determine if the player wins
        result_spin = {
            1: odd_even,
            2: color,
            3: high_low,
            4: number,
        }
        if bet_choice == result_spin[choice]:
            print("Congratulations, you win!")
            result = "win"
        else:
            print("Sorry, you lose.")
            result = "lose"
        
        # Update the player's bank balance
        money = bank_balance(money, bet_amount, result, choice)
        print(f"Your new balance is: {money} tokens.")
        
        if money <= 0:
            print("You are out of money! Game over.")
            break

if __name__ == "__main__":
    main()
