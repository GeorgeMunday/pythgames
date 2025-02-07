import random

def card_gen():
    return random.randint(2,11)
    
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
    dealertotal = dealer_gen()
    if total > 21:
        print("you bust")
    else:
        print(f"dealer has {dealertotal}")
        if total > dealertotal:
            print("you win")
        elif total == dealertotal:
            print("you lose")
        else:
            print("you lose")
    
        
        
    
    

    
if __name__ == "__main__":
    main()