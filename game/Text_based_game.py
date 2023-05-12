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

if Player_Gender=="male":
    Nickname = "hobo"
else:
    Nickname="whore"

Places_1 = ('bar', 'abandoned house')

#First location choice
time.sleep(0.5)
Place_1=input("You decide to walk to a nearby building which turned out to be\n(Bar, Abandoned house)\n").lower()
while Place_1 not in Places_1:
    Place_1 = input('Please choose one of the following ("Bar", "Abandoned house")\n')

# Abandoned house

Abandoned_house_choices_1= ("yes", "no")
Abandoned_house_choices_2= ("run", "attack")

if Place_1=="abandoned house":
            input("You enter the abandoned house trough the window")
            input("Inside i'ts filled with homeless people")
            input("The homeless are begging you for money")
            Abandoned_house_choice_1=input("Do you give them money?\n(Yes, No)\n")
            while Abandoned_house_choice_1 not in Abandoned_house_choices_1:
                Abandoned_house_choice_1=input('Please choose one of the following ("Yes", "no")\n').lower()
            if Abandoned_house_choice_1=="yes":
              input("You split some money between a couple of homeless people but that seemed to attract more people")
              input("You tried to tell them that you didn't have enough money for all of them")
              input("That triggered a rage within the rest of the homeless and they begun attacking you")
              Abandoned_house_choice_2=input("You tried to\n(Deffend, Attack)\n")
              while Abandoned_house_choice_2 in Abandoned_house_choices_2:
                   input("You where overwhelmed and got killed by the homeless")
                   input("Ending: Unfair world")
            if Abandoned_house_choice_1== "no":
                input("You tried to tell them that you didn't have enough money for all of them")
            input("That triggered a rage within the rest of the homeless and they begun attacking you")
            Abandoned_house_choice_2=input("You tried to\n(Deffend, Attack)\n")
            while Abandoned_house_choice_2 in Abandoned_house_choices_2:
                input("You where overwhelmed and got killed by the homeless")
                input("Ending: Be aware of karma")

  #Bar
Bar_choices_2=('who am i?', 'when was the last time i was here?')
if Place_1 == "bar":
            input('You entered the bar to be greeted by a female bartender, in a red silk uniform standing behind the bar')
            input('"You again! Out!" She shouted')
Bar_choices_1=('agressive', 'calm')
Bar_choice_1=input('You decided to be\n(Agressive, Calm)\n').lower()
while Bar_choice_1 not in Bar_choices_1:
            Bar_choice_1=input('Please choose one of the following ("Agressive", "Calm"\n')   

Bar_choices_1=('agressive', 'calm')
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
    
    Bar_choices_2=('who am i?', 'what happened after i trashed the bar?')
    Bar_choice_2=input("you take a seat infront of the barista\n('Who am I?, what happened after i trashed the bar?)\n").lower()
while Bar_choice_2 not in Bar_choices_2:
            Bar_choice_2=input('Please choose one of the following ("who am I?", "what happened after i trashed the bar?")\n')
    
if Bar_choice_2== "what happened after i trashed the bar":
    input("I had to pay!!")
    input("Do you realise how expenisve this bar is??")
    input('"I\'m sorry ok?" She slightly calms down')
    input("Anyways who am I?")
    input('"Some random "' +Nickname)  
    input("with nicer clothes")
     
    input('You flip her off')
       
    input('"I\'m just kidding"')
     
    input('She giggles\nYou\'r probably some criminal that got high and out of controll')
        
    input('"How do you figure?"')
       
    input('"Well you left these guns before you trashed this place"')
        
    input('She grunts while taking multiple guns out from behind the counter')
    input('"I stored them here since their expenisive guns"')
        
    Bar_choices_3=('no', 'yes' )
    Bar_choice_3=input('"So you want them?"\n(Yes, No)\n').lower()
    while Bar_choice_3 not in Bar_choices_3:
    
        Bar_choice_3=input('Please choose one of the following ("Take", "Don\'t take")\n').lower()
        if Bar_choice_3== "no":
            input('"Really?"')
    input('"Yeah, I don\'t think I should continue with this"')
    input('"Especially if I\'m going to end up like this"')
    input('"So what will you do?" She asked')
    input("Well first I need a new job")
    input('She laughed "Good luck with that ex-criminal"')
    input("By the way what's your name?")
    input('"My name is Mia, why do you asked" she said while tucking away the guns behind the counter')
    input('"Well Mia i\'m wondering if your hiring')
    input("Yeah we are, but not criminals")
    input('"Ex-criminal, besides this can be my moment to reedem myself"')
    input('"Fine" she sighed')
    input('"But your not gonna get paid for the first month"')
    input('"Deal" we shook hands, both you and Mia smiled')
    input("Ending: A new chapter")

    if Bar_choice_3 == "yes":
        
        input('"Well i\'m not saying no to free guns"')
        
        input('"Hold on ' +Nickname) 
        input('they aren\'t free"')
        
        input('"Don\'t call me that! "')
        
        input("By the way what's your name?")
        
        input('"I\'m Mia"')

        input('"Okay Mia, what do you want?')
        
        input('"Money"')
        
        input('"How about a little career change instead, you good with guns?"')
        
        input("She smugs")
        
        input("Ending: Partners in crime")    

    
if Bar_choice_2 == "who am i?":
        
            input('"Some random "' +Nickname)  
input("with nicer clothes")
     
input('You flip her off')

input('"I\'m just kidding"')    
input('She giggles\nYou\'r probably some criminal that got high and out of controll')
        
input('"How do you figure?"')
       
input('"Well you left these guns before you trashed this place"')
        
input('She grunts while taking multiple guns out from behind the counter')
input('"I stored them here since their expenisive guns"')
        
Bar_choices_3=('no', 'yes' )
Bar_choice_3=input('"So you want them?"\n(Yes, No)\n').lower()
while Bar_choice_3 not in Bar_choices_3:
            Bar_choice_3=input('Please choose one of the following ("Take", "Don\'t take")\n').lower()
            
            if Bar_choice_3== "no":
                input('"Really?"')
input('"Yeah, I don\'t think I should continue with this"')
input('"Especially if I\'m going to end up like this"')
input('"So what will you do?" She asked')
input("Well first I need a new job")
input('She laughed "Good luck with that ex-criminal"')
input("By the way what's your name?")
input('"My name is Mia, why do you asked" she said while tucking away the guns behind the counter')
input('"Well Mia i\'m wondering if your hiring')
input("Yeah we are, but not criminals")
input('"Ex-criminal, besides this can be my moment to reedem myself"')
input('"Fine" she sighed')
input('"But your not gonna get paid for the first month"')
input('"Deal" we shook hands, both you and Mia smiled')
input("Ending: A new chapter")

if Bar_choice_3 == "yes":
        
            input('"Well i\'m not saying no to free guns"')
        
input('"Hold on ' +Nickname) 
input('they aren\'t free"')
        
input('"Don\'t call me that! "')
        
input("By the way what's your name?")
        
input('"I\'m Mia"')
        
input('"Okay Mia, what do you want?')
        
input('"Money"')
        
input('"How about a little career change instead, you good with guns?"')
        
input("She smugs")
        
input("Ending: Partners in crime")    
