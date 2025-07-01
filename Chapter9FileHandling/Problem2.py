""" 
The game() function in a program lets a user play
a game and return the score as an integer.you need
to read a file "Hiscore.txt" which is either blank 
or contains the previous Hi-score.you need to write 
a program th uppdate the Hi-score whenever game()
breaks the Hi-score.
"""
import random
def game():
        print("You are playing the game")
        score=random.randrange(1,60)
        print(f"Your score : {score}")          
        with open("Hi_score.txt","r") as f:
          maxscore=f.read() 
          if maxscore!="":
           maxscore=int(maxscore)
          else:
            maxscore=0           
        if(score>maxscore):
           with open("Hi_score.txt","w") as f:         
             f.write(str(score))
             print("Highest score saved")
        else :
          print("score low than highest score")   
        return score

game()               