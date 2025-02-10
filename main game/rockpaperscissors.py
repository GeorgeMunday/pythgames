import random

def exit_game():
    # Function to exit the game and return to the main menu
    print("taking you back to main menu")
    return False

def game():
    # Function to play the rock-paper-scissors game
    user_score = 0
    computer_score = 0
    while True:
        choices = ['rock', 'paper', 'scissors']
        rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
        player_choice = input("Enter rock, paper, or scissors or quit to leave: ").lower()
        
        if player_choice == "quit":
            # Exit the game if the player chooses to quit
            exit_game()
            break
        
        if player_choice not in choices:
            # Handle invalid player choices
            print("Invalid choice. Try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            # Handle tie condition
            print("It's a tie!")
            print(f"score is {user_score}:{computer_score}")
        elif rules[player_choice] == computer_choice:
            # Handle player win condition
            print("You win!")
            user_score += 1
            print(f"score is {user_score}:{computer_score}")
        else:
            # Handle player lose condition
            print("You lose!")
            computer_score += 1
            print(f"score is {user_score}:{computer_score}")
        continue

def main():
    # Main function to start the game
    print("welcome to rock paper scissors")
    while True:
        choice2 = input("do you no the rules of the game").lower().strip()
        if choice2 == "yes":
            # Start the game if the player knows the rules
            game()
        else:
            # Explain the rules and start the game
            print("Rock beats scissors, scissors beats paper, paper beats rock. Ties occur if same.")
            game()
        break

if __name__ == "__main__":
    # Entry point of the script
    main()