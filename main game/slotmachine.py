import random
from time import sleep
from colorama import Fore
list1 = ["🍒", "🍋", "🍊", "🍉", "🔔", "💎"]



def machine_result():
    result = random.choice(list1)
    return result

def check_win(result):
    
    if len(set(result)) == 1:
        return 10  
    if "🍋" in result:
        return 1 
    
    return 0

def main():
    bank = 100
    print("Welcome to the slot machine!")
    print(f"You have {bank} tokens.")
    while bank > 0:
        choice1 = input(Fore.WHITE + "Press Enter to pull the lever or type 'quit' to stop playing:").lower()
        if choice1 == 'quit':
            print("Thanks for playing! See you next time.")
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
                print("you win")
            print(f"Your new balance: {bank} tokens")
        else:
            print(Fore.RED + "Invalid input. Please press Enter to spin or type 'quit' to stop.")
    if bank <= 0:
        print(Fore.RED + "You're out of tokens. Game over!")

if __name__ == "__main__":
    main()
