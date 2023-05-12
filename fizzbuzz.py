price=input("Please enter how many poducts you want to buy between 1-5:")
if int(price)<=5:
 calculated_price = int(price) * 100 + 1000 
 print("The price is {}".format( calculated_price))
 vat = int(calculated_price) * 0.10
 calculated_price = vat + calculated_price
 print(" with vat it's {}".format(calculated_price))

else:
 print("No you can only buy 5 products max")



 