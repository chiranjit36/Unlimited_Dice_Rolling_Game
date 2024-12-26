import tkinter as tk
import random

def roll_dice():
    return random.randint(1, 6)

def on_start():
    global game_started
    game_started = True
    roll_button.config(state="normal")
    start_button.config(state="disabled")
    result_label.config(text="🎲 Click 'Roll Dice' to start!")

def on_roll():
    if not game_started:
        return
    dice1 = roll_dice()
    dice2 = roll_dice()
    result_label.config(text=f"🎲 You rolled: 🎲 {dice1} and 🎲 {dice2} 🎲")
    
    if dice1 == 6 and dice2 == 6:
        bonus_roll_button.config(state="normal")
        result_label.config(text="🎉 Double Sixes! Extra roll available! 🎉")
    else:
        bonus_roll_button.config(state="disabled")

def on_bonus_roll():
    bonus1 = roll_dice()
    bonus2 = roll_dice()
    result_label.config(text=f"🎲 Bonus Roll: 🎲 {bonus1} and 🎲 {bonus2} 🎲")
    bonus_roll_button.config(state="disabled")
    roll_button.config(state="normal")

def quit_game():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Ultimate Dice Rolling Game 🎲")
root.geometry("500x350")

# Create widgets
title_label = tk.Label(root, text="🎲 Welcome to the Ultimate Dice Rolling Game! 🎲", font=("Arial", 16), pady=10)
title_label.pack(pady=10)

result_label = tk.Label(root, text="🎲 Click 'Start Game' to begin!", font=("Arial", 12), wraplength=480)
result_label.pack(pady=20)

start_button = tk.Button(root, text="Start Game", command=on_start, font=("Arial", 12), bg="yellow", fg="black", padx=10, pady=5)
start_button.pack(pady=5)

roll_button = tk.Button(root, text="Roll Dice", command=on_roll, font=("Arial", 12), bg="blue", fg="white", state="disabled", padx=10, pady=5)
roll_button.pack(pady=5)

bonus_roll_button = tk.Button(root, text="Bonus Roll", command=on_bonus_roll, font=("Arial", 12), bg="green", fg="white", state="disabled", padx=10, pady=5)
bonus_roll_button.pack(pady=5)

quit_button = tk.Button(root, text="Quit Game", command=quit_game, font=("Arial", 12), bg="red", fg="white", padx=10, pady=5)
quit_button.pack(pady=20)

# Start the GUI loop
game_started = False
root.mainloop()