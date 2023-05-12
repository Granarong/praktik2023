import random
RPS= ("Rock", "Paper", "Scissors")
print("Rock, paper, scissors vs AI")
player=input("Wich one will you pick:  ")

while player not in RPS:

    player=input('Please write down "Rock", "Paper" or "Scissor"\n')
print("The AI Chose")
RPS= ('Rock', 'Paper', 'Scissors')
RPS = random.choice(RPS)
print(RPS)
if player == RPS:
    print("Tie!")
elif player == "Rock" and RPS == "Paper":
    print("Ai wins!")
elif player == "Paper" and RPS == "Rock":
    print("You win!")
elif player == "Rock" and RPS == "Scissors":
    print("You win")
elif player == "Scissors" and RPS == "Rock":
    print("Ai wins!")
