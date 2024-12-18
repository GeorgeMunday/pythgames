import random
from time import sleep


list1 = ["🍒", "🍋", "🍊", "🍉", "🔔", "💎"]



def machine_result():
    result = random.choice(list1)
    return result
def slot_machine():
    for i in range(1):
        position1 = machine_result()
        print(position1, end=" ", flush=True)
        sleep(0.5)

        position2 = machine_result()
        print(position2, end=" ", flush=True)
        sleep(0.5)

        position3 = machine_result()
        print(position3)
        sleep(0.5)
        
        if position1 == position2 == position3:
            print("\n\ud83c\udf89 JACKPOT! You win! \ud83c\udf89")
        elif position1 == position2 or position2 == position3 or position1 == position3:
            print("you kinda win")
        else:
            print("better luck next time")
def main():
    print("welcome to the the slot machiene") 
    slot_machine()  

main() 