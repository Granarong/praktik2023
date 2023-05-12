#Delay
import time

Genders=('male', 'female')
#Start
input("To get the next text press enter, obs when the text has '(---)' please write down the option you want")
input("It's the year 3023, and you just woke up in a wet alley")
input("you squint your eyes in agony looking at the sunrise.")
Player_Name=input("You're starting to remember your name it's\n(Name)\n")


input("You barely remember who you are, and what you were doing.")
Player_Gender=input("You check your reflection on a puddle youre a\n(Male, Female)\n").lower()
while Player_Gender not in Genders:
    Player_Gender=input('Please choose one of the following ("Male", "Female")\n')
input("You notice that you have quiet fancy clothes, but your hair is greasy, indicating you slept outside")

Places_1 = ('bar', 'strip club' , 'drug house')

#First location choice
time.sleep(0.5)
Place_1=input("You decide to walk to a nearby building which turned out to be\n(Bar, Strip club, 'Drug house)\n").lower()
while Place_1 not in Places_1:
    Place_1 = input('Please choose one of the following ("Bar", "Strip club", "Drug house")\n')

#Bar
Bar_choices_1=('agressive', 'calm')
Bar_choices_2=('who am i?', 'when was the last time i was here?')


if Place_1 == "bar":
    input('You entered the bar to be greeted by a female bartender standing behind the bar')
    input('"You again! Out!" She shouted')
    Bar_choice_1=input('You decided to be\n(Agressive, Calm)\n').lower()
    while Bar_choice_1 not in Bar_choices_1:
        Bar_choice_1=input('Please choose one of the following ("Agressive", "Calm"\n')   

if Bar_choice_1 == "agressive":
    input('"Stop screaming you bitch!!')
    input('She picks up a gun from under the counter')
    input('"I would like to apo..."\nA gunshot was heard from the bar')
    input('You are dead\nEnding:Let\'s calm down shall we')
    
if Bar_choice_1=="calm":
    input("Last time you were here you trashed the place!!")
    input("Look i'm sorry okay?")
    input("Fine... I geuss it's okay since you were high")
    input("I was high?")
    time.sleep(0.5)
    print("Yeah and you were screaming about how you were "+Player_Name,"the ruler") 
    Bar_choice_2=input("you take a seat infront of the barista\n('Who am I?, When was the last time i was here?)\n").lower()
while Bar_choice_2 not in Bar_choices_2:
    Bar_choice_2=input('Please choose one of the following ("who am I?", "what happened after i trashed the bar?)"\n')
    if Bar_choice_2 == "who am i?":
        
        input("Some random hobo with nicer clothes")
     
        input('You flip her off')
       
        input('"I\'m just kidding"')
     
        input('She giggles\nYou\'r probably some criminal that got high and out of controll')
        
        input('"How do you figure?"')
       
        input('"Well you left these guns before you trashed this place"')
        
        input('She grunts while taking multiple guns out from behind the counter')
        input('"I stored them here since their expenisive guns"')