import random

s=1
e=6
while True:
    i = input("\nEnter 'R' to roll the dice Or Enter 'Q' to exit: ").strip().upper()
    if i =="R":
        d = random.randint(s,e)
        print(f"\nYou Rolled {d} in Dice.")
        if d==6:
            d1=random.randint(s,e)
            print(f"You Rolled {d1} in Dice.")
    elif i=="Q":
        break

