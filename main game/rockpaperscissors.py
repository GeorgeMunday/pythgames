import random

def exit_game():
    print("taking you back to main menu")
    return False

def game():
    user_score = 0
    computer_score = 0
    while True:
        choices = ['rock', 'paper', 'scissors']
        rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
        player_choice = input("Enter rock, paper, or scissors or quit to leave: ").lower()
        
        if player_choice == "quit":
            exit_game()
            break
        
        if player_choice not in choices:
            print("Invalid choice. Try again.")
            continue
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if player_choice == computer_choice:
            print("It's a tie!")
            user_score += 1
            computer_score += 1
            print(f"score is {user_score}:{computer_score}")
        elif rules[player_choice] == computer_choice:
            print("You win!")
            user_score += 1
            print(f"score is {user_score}:{computer_score}")
        else:
            print("You lose!")
            computer_score += 1
            print(f"score is {user_score}:{computer_score}")
        continue

def main():
    print("welcome to rock paper scissors")
    while True:
        choice2 = input("do you no the rules of the game").lower().strip()
        if choice2 == "yes":
            game()
        else:
            print("Rock beats scissors, scissors beats paper, paper beats rock. Ties occur if same.")
            game()
        break

if __name__ == "__main__":
    main()