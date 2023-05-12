start=input("Start at: ")
stop=input("Stop at: ")

#Todo input antal steg

# Skatten i procent %
for price in range (int(start), int(stop),100): 
  vat=price * 0.10
  tot= price + vat
  print("Total price" , tot)
