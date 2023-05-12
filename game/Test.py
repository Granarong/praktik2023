#Delay
import time
#Score system


score = 0
Anwers= ('an candle','candle')
correct_answers = {"my name", "your name", "2023"}
Hitler= {"suicide", "he killed himself", "he commited suicide"}
Candle ={"a candle", "candle"}

#The quiz
print("Quiz time")
player=input("Do you want to play?: ").lower()
if player == "yes": 
 
 time.sleep(0.5)
 print("Ok, let's do it!")
else:
     time.sleep(0.5)
     print("Kidding, you have no choice") 


time.sleep(0.5)
name=input("Let's start easy what's your name?\n")
if name == "Cheat":
    print("Answers:\nGermany\n1939\nSuicide\ny\nMy name\nTeknikringen 7\nStockholm\nA candle")
time.sleep(0.5)
print("Ok " + name)
answer=input("Where did the Nazi originate from? \n").lower()
if answer == "germany":
    time.sleep(0.5)
    print("Nice,+1 point")
    score +=1
else:
    time.sleep(0.5)
    print("Sry, thats wrong, no point for you")

time.sleep(0.5)
print("next question")
time.sleep(0.5)
answer=input("What year did ww2 start?\n").lower()
if answer=="1939":
    time.sleep(0.5)
    print("Nice, you know basic history,+1 point")
    score +=1
else:
    time.sleep(0.5)
    print("Wroong, it's good to know that, but you can't know everything I guess")

time.sleep(0.5)
print("On to the third question ")

time.sleep(0.5)
hitler=input("How did hitler die?\n").lower()
if hitler in Hitler:
 time.sleep(0.5)
 print("That is a point for you!")
 score +=1
else:
 time.sleep(0.5)
 print("Don't worry we're moving on from history")
 time.sleep(0.5)
 print("Now it's time for some riddles")

time.sleep(0.5)
answer=input("What is in the middle of eye?\n").lower()
if answer=="y":
    time.sleep(0.5)
    print('Nice, +1 point')
else:
    time.sleep(0.5)
    print('Notice that I did\'nt say "The eye"')

time.sleep(0.5) 
print("Ok, you're halfway trough")

time.sleep(0.5)
Namn=input("what is yours, but others most likely use it more than you?\n").lower()

if Namn in correct_answers:
    time.sleep(0.5)
    print("your quite intellect " + name, ",+1 point")
    score +=1
else:
    print("Remember the first question" + name,"!?")

time.sleep(0.5)
print("You should know this next question")
answer=input("What street of Sigma Connectivity located on?\n").lower()
if answer== "teknikringen 7":
    time.sleep(0.5)
    print("Phew, you knew that one, +1 point")
    score +=1
else: 
    time.sleep(0.5)
    print("Ehmm....")

time.sleep(0.5)
print("Second to last question now")
answer=input("What is Sweden's biggest city?\n").lower()
if answer == "stockholm":
    time.sleep(0.5)
    print("Correct! +1 point")
    score +=1
else:
    time.sleep(0.5)
    print("Ok, I used google, so maybe i'm wrong and not you")

time.sleep(0.5)
print("The final question")
time.sleep(0.5)
candle = input("It's tall when it's young, and it's short when it's old, what is it?\n").lower()
if candle in candle:
    time.sleep(0.5)
    print("Ok ok I see, you're smart " + name, "+1 point")
    score +=1

else:
    time.sleep(0.5)
    print("To be fair it only makes sens if I stated that it was burning")

time.sleep(0.5)
print("Ok this is the end of the quiz, lets see your score \n" + str(score),"/8")
if score == 0:
    print('Try writing this down when it asks you for your name: "Cheat"')
