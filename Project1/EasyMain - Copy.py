import random
choices = {"snake": 1, "water": -1, "gun": 0}
reverse_map = {1: "Snake", -1: "Water", 0: "Gun"}
winning_cases = {
    (1, -1): "win",
    (-1, 0): "win",
    (0, 1): "win",
}
you_input = input("Enter your choice (snake, gun, water): ").strip().lower()
if you_input not in choices:
    print("Invalid choice! Please choose from snake, gun, or water.")
else:
    you = choices[you_input]
    computer = random.choice([-1, 0, 1])

    print(f"\nYou chose      : {reverse_map[you]}")
    print(f"Computer chose : {reverse_map[computer]}\n")

    if you == computer:
        print("It's a draw!")
    elif (you, computer) in winning_cases:
        print("You win!")
    else:
        print("You lose!")
