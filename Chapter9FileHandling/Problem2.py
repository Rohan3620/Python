""" 
The game() function in a program lets a user play
a game and return the score as an integer.you need
to read a file "Hiscore.txt" which is either blank 
or contains the previous Hi-score.you need to write 
a program th uppdate the Hi-score whenever game()
breaks the Hi-score.
"""
def game():
    i=int(input("Enter score "))
    return i;
f=open("Hi_score.txt","+a")
str="High score"

a=game()
f.write(a)