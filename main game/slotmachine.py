import random
from time import sleep

list1 = ["🍒", "🍋", "🍊", "🍉", "🔔", "💎"]

def machine_result():
    result = random.choice(list1)
    return result

def main():
    bank = 100
    while bank > 0:
        print("Welcome to the slot machine!")
        print(f"You have {bank} tokens.")
        
        choice1 = input("Press Enter to pull the lever or type 'quit' to stop playing:").lower()
        if choice1 == "":
            result = []
            for _ in range(5):
                position = machine_result()
                result.append(position)
                print(position, end=" ", flush=True)
                sleep(0.5)
            print()


    if bank <= 0:
        print("You're out of tokens. Game over!")

if __name__ == "__main__":
    main()