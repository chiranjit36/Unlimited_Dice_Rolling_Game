import random

def roll_dice():
    return random.randint(1, 6)

print("🎲 Welcome to the Ultimate Dice Rolling Game! 🎲")
print("------------------------------------------------")

while True:
    choice = input("\nEnter 'R' to Roll the Dice or 'Q' to Quit: ").strip().upper()
    if choice == "R":
        dice1 = roll_dice()
        dice2 = roll_dice()
        print(f"\n✨ You rolled: 🎲 {dice1} and 🎲 {dice2} ✨")
        
        if dice1 == 6 and dice2 == 6:
            print("🎉 Jackpot! Double Sixes! You get an extra roll! 🎉")
            bonus1 = roll_dice()
            bonus2 = roll_dice()
            print(f"\nBonus Roll: 🎲 {bonus1} and 🎲 {bonus2} 🎲")
            
    elif choice == "Q":
        print("\nThank you for playing! Goodbye! 👋")
        break
    else:
        print("\nInvalid input. Please enter 'R' to roll or 'Q' to quit.")
