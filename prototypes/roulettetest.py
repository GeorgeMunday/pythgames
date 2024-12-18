import random
import time

def result_game():
    return random.randint(0, 36)

def play_again(bank):
    print("-" * 40)
    if bank == 0:
        exit_game(bank)
    else:
        choice3 = input("Do you want to play again (yes/no):").lower()
        if choice3 == "yes":
            roulette(bank)
        else:
            exit_game(bank)

def exit_game(bank):
    print("-" * 40)
    profit = bank - 100
    print(f"You profited £{profit}")
    exit()

def roulette(bank):
    print(f"You have £{bank} in your bank.")
    bet = input("How much would you like to bet? £")
    print("-" * 40)
    if bet == "0":
        exit_game(bank)
    else:
        if bet.isnumeric():
            bet = int(bet)
            bank -= bet
            choice1 = input("What would you like to bet on:\n 1. Colour\n 2. Odd or Even\n 3. Number")
            print("-" * 40)
            result = result_game()

            while choice1 == "1":  # Colour betting
                print("-" * 40)
                print(f"You have £{bank} in your bank.")
                choice2 = input("Would you like to bet on red or black? ").lower()
                print("Spinning...")
                time.sleep(1)
                print(f"It landed on {result}")

                # Color determination based on the number (simplified logic)
                if result == 0:
                    condition = "green"
                elif result % 2 == 0:
                    condition = "red"
                else:
                    condition = "black"

                print(f"It is {condition}.")
                if condition == choice2:
                    print("You win!")
                    bank += bet * 2
                else:
                    print("You lose!")

                play_again(bank)
                break

            while choice1 == "2":  # Odd or Even betting
                print(f"You have £{bank} in your bank.")
                choice2 = input("Would you like to bet on odd or even? ").lower()
                print("Spinning...")
                time.sleep(1)
                print(f"It landed on {result}")

                if result % 2 == 0:
                    condition = "even"
                    print(f"It is {condition}.")
                else:
                    condition = "odd"
                    print(f"It is {condition}.")

                if condition == choice2:
                    print("You win!")
                    bank += bet * 2
                else:
                    print("You lose!")

                play_again(bank)
                break

            while choice1 == "3":  # Number betting
                print(f"You have £{bank} in your bank.")
                choice2 = input("What number do you want to bet on (0-36)? ")
                if not choice2.isdigit() or int(choice2) < 0 or int(choice2) > 36:
                    print("Invalid number.")
                    roulette(bank)
                    break

                choice2 = int(choice2)
                print("Spinning...")
                time.sleep(1)
                print(f"It landed on {result}")

                if result == choice2:
                    print("You win!")
                    bank += bet * 36
                else:
                    print("You lose!")

                play_again(bank)
                break

        else:
            print("Invalid input.")
            roulette(bank)

def main():
    bank = 100
    print(f"\nYou are starting with £{bank}. Let's play Roulette!\n try your luck for a big win")
    print("-" * 40)
    while True:
        play = input("Are you over the age of 18? (yes/no):").lower()
        if play == "yes":
            print("-" * 40)
            roulette(bank)
        elif play == "no":
            print("\nYou are not of legal age to play this game.")
            
        else:
            print("\nInvalid input")
            
if __name__ == "__main__":
    main()