stock = ['pepperoni', 'sausage', 'cheese', 'pepper']
size = ['large', 'medium', 'small']
drink = ['coke', 'pepsi', 'sprite', 'fanta']
order = input("please give us a topping: ")
#list
list = []
if order in stock:
	print(f"we have {order}")
	list.append(order)
else: 
	print(f"sorry we don't have {order}")
while len(list) != 2:
	orderPhir = input("plese gimme a one more topping: ")
	if orderPhir in stock:
		print(f"we have {orderPhir}")
		list.append(orderPhir)
	else:
		print(f"we dont have {orderPhir}")
print("here are your toppings: ", list)
#size
sizeInput = input("What size: ", )
if sizeInput in size:
	print(f"mama {sizeInput} hai ")
else:
	print(f"mama {sizeInput} nai hai")
#drink
print("apne pass drinks ye hai", drink)
drinkInput = input("bolo kya hona mama: ", )
if drinkInput in drink:
	print(f"{drinkInput} peete mama tum")
else: 
	print(f"ahre wo nai hai na mama aj")

#overview
print(f"acha ek baar bolrao dekhlo sahi hai kya topping: {list}, phir size {sizeInput}, aur drink me {drinkInput}")

