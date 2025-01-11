import random
from time import sleep
from colorama import Fore
def place_bet(choice):
    choice2 = ""
    bank = 100
    answer = ["odd","even"]
    answer1 = ["red","black"]
    answer2 = ["high","low"]
    options = {
        1: "pick odd or even",
        2: "pick red or black",
        3: "pick high or low",
        4: "pick a number between 0 and 36",
    }
    while True:
        choice1 = int(input("you have 100 tokens, how many tokens would you like to bet? "))
        if choice1 > bank:
            print("you do not have enough tokens")
            continue
        else:
            print(f"you have bet {choice1} tokens")
            print(options.get(choice, "invalid choice"))
            choice2 = input("Enter your choice:").lower().strip()
            if choice == 1 and choice2 in answer:
                return "choice2"
            elif choice == 2 and choice2 in answer1:
                return choice2
            elif choice == 3 and choice2 in answer2:
                return choice2
            elif choice == 4 and choice2.isnumeric() and 0 <= int(choice2) <= 36:
                return int(choice2)
def result(choice):
   #Simulate a spin of the roulette wheel.
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
        choice = (input(
                "What would you like to bet on? \n"
                "1. Odd or Even \n"
                "2. Red or Black \n"
                "3. High or Low \n"
                "4. Specific Number \n"
                "5. Quit \n"
                "Enter your choice: "))
        if choice == 5:
            print("taking you back to main menu")
            return False
        if choice.isnumeric() == False and choice not in [1,2,3,4]:
            print("invalid choice")
            break
        else:
            choice = int(choice)
            roulette = result(choice)
            player_choice = place_bet(choice)
            print(f"The result is: {roulette}")
            if player_choice == roulette:
                print("you win")
                continue
            else:
                print("you lose")
                continue
if __name__ == "__main__":
    main()