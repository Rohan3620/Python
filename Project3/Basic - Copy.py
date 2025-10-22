import random
computer=random.randint(1,100)
guesses=0
while True:
    player=int(input("Guess the number between 1 to 100 : "))
    guesses+=1
    if player==computer:
        print("You Win")
        break
    elif player<computer:
        print("Enter a big number ")
    elif player>computer:
        print("Enter a small number ")
print(f"You have gussed the number correctly in {guesses} attempt")
