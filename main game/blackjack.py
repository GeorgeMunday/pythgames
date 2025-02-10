import random
from time import sleep
from colorama import Fore

def loading():  # Prints "loading..." and pauses for one second each time it's called, to avoid the process being instant
    print("loading...")
    sleep(1)  # Pause for 1 second
    print("-" * 40)  # Print a separator line
    
def card_gen():
    return random.randint(2,11)

def exit_game(bank):
    if bank < 0:
        print("exiting game")
        return   
    choice = input("do you want to exit the game?")
    if choice == "yes":
        print("exiting game")
        return
    
def dealer_gen():
    dealer_card1= card_gen()
    dealer_card2= card_gen()
    temp_card= card_gen()
    total = dealer_card1 + dealer_card2
    print(f"dealer has {dealer_card1} and {dealer_card2 } this totals to {total}")
    while 21 > total < 17:
        total = total + temp_card
        print(f"then he got {temp_card} witch totals to {total} ")
        if total == 20 or total == 19:
            break
    dealer_total = total
    if total > 21:
        return "bust"
    return dealer_total

def main():
    bank = 100
    print("welcome to blackjack")
    while True:
        print(f"you have {bank} tokens")
        bet = (input("how much would you like to bet?"))
        if bet.isnumeric() == False or int(bet) > bank:
            print("invalid inptut")
            continue
        bet = int(bet)
        print(f"you have bet {bet}")
        bank = bank - bet
        card1= card_gen()
        card2= card_gen()
        temp_card= card_gen()
        total = card1 + card2
        choice = "hit"
        print(f"your cards are {card1} and {card2} this totals to {total}")
        
        while choice == "hit" and total < 21:
            choice = input("do you want to hit or hold")
            if choice == "hit":
                total = total + temp_card
                print(total)
                continue
            elif choice == "hold":
                break
            else:
                print("invald choice")
                continue
        loading()
        dealertotal = dealer_gen()
        if total > 21:
            print("you bust")
        else:
            print(f"dealer has {dealertotal}")
            if total > dealertotal:
                print("you win")
                bet = bet*2
                bank = bank + bet
            elif total == dealertotal:
                print("you lose")
                bank = bank - bet
            else:
                print("you lose")
                bank = bank - bet
        exit_game(bank)

if __name__ == "__main__":
    main()