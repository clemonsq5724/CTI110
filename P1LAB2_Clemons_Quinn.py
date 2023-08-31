"""
CTI110
P1LAB2 -sales
Quinn Clemons
8/31
Simple point of sales program


"""
# set up our store

store_name = "Maniac Productions"
product = "beats"
stock = 50
price = 99.99

# Greet Customer

print("Welcome to",store_name)
print("How are you, what's your name?")
customer_name = input()
print("Nice to meet you", customer_name)

# Explain Product
print("We have a great deal on our new:", product)
print("the deal going on for today is: $", price)
print("hurry up and catch this great deal, their is only", stock, "available!!")

# take order

print("how many", product, "would you like to buy?")
# input gives us a string
#order = input()
# convert it to a number
#order = int(order)

# or....

order = int(input())


# finish up
# optional

if (order > stock):
  order = stock
  print("sorry, we can only sell you", order)

total_price = order * price
print("so you would like")
print(order,product, "for a total of $", total_price, "?")

print("<y/n>" ,sep="")
confirm = input()
if (confirm =="y"):
  print("shipped!")
else:
  print("order canceled.")

print("Thanks for making your purchase with", store_name, "!")





