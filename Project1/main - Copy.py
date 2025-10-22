import random
"""
Snake drinks water → Snake wins ✅
Water drowns gun → Water wins ✅
Gun kills snake → Gun wins ✅
project 1
1 for sanke
-1 for water
o for gun 
"""
computer=random.choice([-1,0,1])
youstr =input("Enter your choice Snake,gun,water: ").lower().strip()
youDict={"snake":1,"water":-1,"gun":0}
revdic={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[youstr]
print(f"You choice : {revdic[you]}\nComputer chose : {revdic[computer]} ")
if(computer==you):
    print("It is draw")
else:        
      if(computer==-1 and you==1):
          print("You win!")
      elif(computer==-1 and you==0):
          print("You Lose!")
      elif(computer==1 and you==-1):
          print("You lose!")
      elif(computer==1 and you==0):
          print("You win!")
      elif(computer==0 and you==-1):
          print("You win!")
      elif(computer==0 and you==1):
          print("You lose!")
      else:
           print("Something went wrong")        
