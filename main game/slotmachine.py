import random
from time import sleep
from colorama import Fore

# List of slot machine symbols
list1 = ["🍒", "🍋", "🍊", "🍉", "🍎", "🍍", "🍇", "🍓"]

# Function to get a random result from the slot machine
def machine_result():
    result = random.choice(list1)
    return result

# Function to check if the player has won
def check_win(result):
    # Check if all three symbols are the same
    if len(set(result)) == 1:
        return 10  # Return 10 tokens for three of a kind
    # Check if there is a lemon in the result
    if "🍋" in result:
        return 3  # Return 3 tokens for a lemon

    return 0  # Return 0 tokens if no win

def main():
    bank = 100  # Initial number of tokens
    print("Welcome to the slot machine! the goal of the game is to get a lemon or three of a kind")
    print(f"You have {bank} tokens.")
    while bank > 0:
        choice1 = input(Fore.WHITE + "Press Enter to pull the lever or type 'quit' to stop playing:").lower()
        if choice1 == 'quit':
            print("taking you back to main menu.")
            break
        elif choice1 == "":
            bank -= 1  # Deduct 1 token for each spin
            result = []
            for _ in range(3):
                position = machine_result()
                result.append(position)
                print(position, end=" ", flush=True)
                sleep(0.5)
            print()
            
            # Check if the player won
            win = check_win(result)
            if win > 0:
                bank += win  # Add winnings to bank
                print(f"Congratulations! You won {win} tokens!")
            else:
                print("you lose")
            print(f"Your new balance: {bank} tokens")
        else:
            print(Fore.RED + "Invalid input. Please press Enter to spin or type 'quit' to stop.")
    if bank <= 0:
        print(Fore.RED + "You're out of tokens. Game over! taking you back to main menu")

if __name__ == "__main__":
    main()
