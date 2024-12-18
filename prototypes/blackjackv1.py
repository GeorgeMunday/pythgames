import random
def end_game(bank):
    profit = bank - 100
    print(f"you profited £{profit}")
    exit()
    
def game(bank):
    bet = 0
    card1 = 0
    card2 = 0
    card3 = 0
    total = 0
    status = ""
    exit_game = ""
    
    print(f"\n You have £{bank} left in your bank.\n")
    bet =input("How much would you like to bet? £")
    if bet == "0" :
        end_game(bank)                      
    else:
        if bet.isnumeric(): 
            bet = int(bet)
            while True:
                # Deduct the bet from the bank
                bank -= bet
                print(f"\n You have £{bank} left in your bank.\n")
                
                # Set up the deck of cards
                deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
                
                # Dealer's initial cards
                dealer_card1 = random.choice(deck)
                dealer_card2 = random.choice(deck)
                dealer_total = dealer_card1 + dealer_card2
                
                print(" Dealer's turn:")
                print(f"  Dealer has {dealer_card1} and a hidden card.")
                
                # Player's initial cards
                card1 = random.choice(deck)
                card2 = random.choice(deck)
                total = card1 + card2
                
                print("\n Your cards:")
                print(f"  You drew: {card1} and {card2}. Total: {total}\n")
                
                # Handle Ace card for the player
                if total > 21 and (card1 == 11 or card2 == 11):
                    total -= 10  # Adjust Ace value
                    print(f" Your total exceeds 21. Adjusting Ace to 1. New total: {total}\n")
                
                # Player's turn
                while total < 21:
                    status = input("Do you want to 'hold' or 'hit'? ").lower()
                    
                    if status == "hit":
                        card3 = random.choice(deck)
                        total += card3
                        print(f" You drew: {card3}. Your total is now: {total}")
                        if total > 21:
                            print("You bust!")
                            break
                    elif status == "hold":
                        print(f" You hold with a total of {total}")
                        break
                    else:
                        print(" Invalid choice! Please choose 'hold' or 'hit'.")
                
                # Dealer's turn if the player hasn't busted
                if total <= 21:
                    print(f"\n Dealer reveals cards: {dealer_card1} and {dealer_card2}. Total: {dealer_total}")
                    while dealer_total < 17:
                        dealer_card3 = random.choice(deck)
                        dealer_total += dealer_card3
                        print(f" Dealer drew: {dealer_card3}. Dealer's total is now: {dealer_total}")
                    
                    # Determine the outcome
                    if dealer_total > 21:
                        print("\n Dealer busts! You win!")
                        bank += bet * 2
                    elif dealer_total > total:
                        print("\n Dealer wins!")
                    elif dealer_total < total:
                        print(f"\n You win! Your total of {total} beats the dealer's total of {dealer_total}.")
                        bank += bet * 2
                    else:
                        print("\n It's a tie!")
                
                # Ask if the player wants to play again
                if bank <= 0:
                    print(" You have no more money left. Exiting...")
                    end_game(bank)
                
            
                exit_game = input("\n Do you want to play again? (yes/no): ").lower()
                if exit_game == "no":
                    print(" Thanks for playing! Exiting the game...")
                    end_game(bank)
                    break
                elif exit_game == "yes":
                    while True:
                        choice1 = input("do you want to chnge your bet (yes/no)?").lower()
                        if choice1 == "yes":
                            bet = int(input("what do you want to change it to"))
                            break
                        elif choice1 == "no":
                            bet = bet
                            break
                        else:
                            print("invalid input")
                    print("\ninvalid input")
        elif bet == 0:
            print("\n Invalid input for bet amount. Please try again.")
        else:
            print("\n Invalid input for bet amount. Please try again.")
        return bank

def main():
    bank = 0
    play = ""
    
    # Welcome message
    print("\n Welcome to Blackjack! ")
    print(" Try your luck and win big! ")
    print("-" * 40)
    
    play = input("Are you over the age of 18? (yes/no): ").lower()
    if play == "yes":
        play = True
    elif play == "no":
        print("\n You are not of legal age to play this game.")
        return
    else:
        print("\nInvalid input. Please restart the game.")
        return
    
    while play:
        bank = 100
        print(f"you have this much in your bank{bank}")
        game(bank)
       
          
# Run the game
if __name__ == "__main__":
    main()
