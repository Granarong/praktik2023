
import time

#Score system p1

Player_points = 0
RPS_points = 0
Tie_points = 0

#Titel
print("Rock, Paper, Scissors VS AI\nbest of 3")

#Player choice
for i in range(3):
 player = input("What will you pick? \n").lower()
 RPS = ('rock', 'paper', 'scissors')
 while player not in RPS:
    player =input('Please choose "Rock", "Paper" or "Scissors" \n').lower()

 #Randomiser
 import random 
 import time

 RPS = ('rock', 'paper', 'scissors')
 RPS = random.choice(RPS)
 print("Ai chose...") 
 time.sleep(1.3)
 print(RPS) 


 #Win/lose
 time.sleep(0.7)
 if player==RPS:
    print("Tie")
    Tie_points +=1
 elif player == "rock" and RPS == "scissors":
    print("You win!")
    Player_points += 1
 elif player == "scissors" and RPS == "rock":
    print("AI wins!")
    RPS_points += 1
 elif player == "paper" and RPS == "scissors":
    print("Ai wins!")
    RPS_points += 1 
 elif player =="paper" and RPS == "rock":
    print("You win!")
    Player_points += 1
 elif player == "rock" and RPS == "paper":
    print("Ai wins!") 
    RPS_points += 1
 elif player == "scissors" and RPS == "paper":
    print("You win")
    Player_points += 1
    
# Score System p2    
time.sleep(0.8)
print("Score")
print("you:" + str(Player_points))  
print("AI:" + str(RPS_points))
if Tie_points >=1:
   print("Tie:" + str(Tie_points))
if Player_points > RPS_points:
   print("You won!!")
else:
   print("AI has won, unlucky")
print("Thank you for playing")