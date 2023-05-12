##Own version
Method = ("'+', '-', '*',' '/'")
user=input("What method would you like to use\nPlease use one of the following (+, -, *, /)\n")
for i in range(1000000):
 while user not in Method:
     user=input("Please choose one of the following, (+, -, *, /)")
 number_1= float(input("First number\n"))
 number_2= float(input("Second number\n"))

 if user == "+": 
    print(number_1, "+", number_2, "=",(number_1 + number_2))

 elif user== "-": 
    print (number_1, "-", number_2, "=",(number_1 - number_2))

 elif user== "*":
    print(number_1, "*", number_2, "=",(number_1 * number_2))

 elif user== "/":
      print(number_1, "/", number_2, "=",(number_1 / number_2))
 again=input("Do you want to do another calculation?\n(Yes/No)\n").lower()
 if again != "yes":
   break