import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import os
import winsound

# Constants
SNAKE = 1
WATER = -1
GUN = 0

choices = {"snake": SNAKE, "water": WATER, "gun": GUN}
reverse_map = {SNAKE: "Snake 🐍", WATER: "Water 💧", GUN: "Gun 🔫"}
winning_cases = {
    (SNAKE, WATER): "win",
    (WATER, GUN): "win",
    (GUN, SNAKE): "win",
}

# Globals
user_score = 0
computer_score = 0
rounds_played = 0
max_rounds = 5
sound_on = True
leaderboard_file = "leaderboard.txt"

# GUI setup
root = tk.Tk()
root.title("Snake 🐍 Water 💧 Gun 🔫")
root.geometry("460x430")
root.resizable(False, False)

# Sound control
def play_sound(result):
    if not sound_on:
        return
    if result == "win":
        winsound.Beep(800, 200)
    elif result == "lose":
        winsound.Beep(400, 200)
    elif result == "draw":
        winsound.Beep(600, 200)

def toggle_sound():
    global sound_on
    sound_on = not sound_on
    sound_button.config(text=f"Sound: {'ON' if sound_on else 'OFF'}")

# Background flash
def flash_result(color):
    original_color = root.cget("bg")
    root.config(bg=color)
    root.after(200, lambda: root.config(bg=original_color))

def set_buttons_state(state):
    for child in button_frame.winfo_children():
        child.config(state=state)

# Leaderboard
def save_score(name, score):
    with open(leaderboard_file, "a") as f:
        f.write(f"{name}:{score}\n")

def show_leaderboard():
    if not os.path.exists(leaderboard_file):
        messagebox.showinfo("Leaderboard", "No scores yet.")
        return
    with open(leaderboard_file, "r") as f:
        scores = [line.strip().split(":") for line in f.readlines()]
        scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)[:3]
        msg = "\n".join([f"{i+1}. {name} - {score}" for i, (name, score) in enumerate(scores)])
        messagebox.showinfo("🏆 Leaderboard - Top 3", msg)

# Change round limit via button
def change_rounds():
    global max_rounds
    new_val = simpledialog.askinteger("Set Rounds", "Enter number of rounds (1–20):", minvalue=1, maxvalue=20)
    if new_val:
        max_rounds = new_val
        reset_game()

# Game logic
def play(user_choice):
    global user_score, computer_score, rounds_played

    if rounds_played >= max_rounds:
        result_label.config(text="🎯 Game over! Reset to play again.", fg="blue")
        return

    user = choices[user_choice]
    computer = random.choice([SNAKE, WATER, GUN])

    user_choice_label.config(text=f"You chose: {reverse_map[user]}")
    computer_choice_label.config(text=f"Computer chose: {reverse_map[computer]}")

    if user == computer:
        result = "draw"
        result_label.config(text="🤝 It's a draw!", fg="orange")
    elif (user, computer) in winning_cases:
        result = "win"
        user_score += 1
        result_label.config(text="🎉 You win this round!", fg="green")
    else:
        result = "lose"
        computer_score += 1
        result_label.config(text="😢 You lose this round!", fg="red")

    play_sound(result)
    flash_result("lightgreen" if result == "win" else "lightcoral" if result == "lose" else "lightyellow")

    rounds_played += 1
    score_label.config(text=f"Round {rounds_played}/{max_rounds} | You: {user_score} | Computer: {computer_score}")

    if rounds_played == max_rounds:
        set_buttons_state("disabled")
        if user_score > computer_score:
            msg = "🏆 You won the game!"
            name = simpledialog.askstring("Name", "Enter your name for the leaderboard:")
            if name:
                save_score(name, user_score)
        elif user_score < computer_score:
            msg = "💀 Computer wins the game!"
        else:
            msg = "⚖️ It's a tie game!"
        messagebox.showinfo("Game Over", msg)

# Reset game
def reset_game():
    global user_score, computer_score, rounds_played
    user_score = 0
    computer_score = 0
    rounds_played = 0
    score_label.config(text=f"Round 0/{max_rounds} | You: 0 | Computer: 0")
    user_choice_label.config(text="")
    computer_choice_label.config(text="")
    result_label.config(text="")
    root.config(bg="SystemButtonFace")
    set_buttons_state("normal")

# UI layout
tk.Label(root, text="Snake 🐍 Water 💧 Gun 🔫", font=("Arial", 18, "bold")).pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Snake 🐍", width=10, command=lambda: play("snake")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Water 💧", width=10, command=lambda: play("water")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Gun 🔫", width=10, command=lambda: play("gun")).grid(row=0, column=2, padx=5)

user_choice_label = tk.Label(root, text="", font=("Arial", 12))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="", font=("Arial", 12))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Round 0/5 | You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=5)

control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Button(control_frame, text="Reset", width=10, command=reset_game).grid(row=0, column=0, padx=5)
tk.Button(control_frame, text="Set Rounds", width=10, command=change_rounds).grid(row=0, column=1, padx=5)
tk.Button(control_frame, text="Leaderboard", width=10, command=show_leaderboard).grid(row=0, column=2, padx=5)
tk.Button(control_frame, text="Exit", width=10, command=root.quit).grid(row=0, column=3, padx=5)

sound_button = tk.Button(root, text="Sound: ON", width=12, command=toggle_sound)
sound_button.pack(pady=5)

# Start game
reset_game()
root.mainloop()
