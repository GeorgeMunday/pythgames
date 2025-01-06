import random

def spin (level):
    
    if level == 1:
        return random.randint(1,10)
    elif level == 2:
        return random.randint(1,50)
    elif level == 3:
        return random.randint(1,100)
    elif level == 4:
        return random.randint(1,250)
    elif level == 5:
        return random.randint(1,1000)
    else:
        print("Invalid level!")
        return None
    
def exit_game():
    choice = input("would you like to continue (yes/no)")
    if choice == "no":
        exit()
    else:
        print("-" * 40)
        main()

def main():
    choice1 = 0
    level = 0
    count = 0
    while True:
        print("Welcome to number guess game!!")
        level = int(input("what level would you like to play 1 or 2\nEnter here:"))
        number = spin(level)
        if number is None:
            return
        
        options = {
        "1":"pick a number between 1 and 10",
        "2":"pick a number between 1 and 50",
        "3":"pick a number between 1 and 100",
        "4":"pick a number between 1 and 250",
        "5":"pick a number between 1 and 1000"
        
    }
        print(options[level])
        
        while level == 1 or level == 2 or level == 3 or level == 4 or level == 5:
            print("")
            count = count +1
            if 1 < choice1 > 5:
                choice1 = int(input("pick your number\n Enter here:"))
                if number == choice1:
                    print(f"it was {number} you win!! ")
                    print(f"you did it in {count} turns")
                    exit_game()
                elif number > choice1:
                    print("pick a higher number")
                else:
                    print("pick a lower number")
        
            
        
        
        
   
    
    
    
    
if __name__ == "__main__":
    main()