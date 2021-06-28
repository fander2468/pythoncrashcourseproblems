
pizza_toppings = ''
while pizza_toppings != 'quit':
    pizza_toppings = input("Enter a pizza topping, enter 'quit' to quit ")
    if pizza_toppings == 'quit':
        continue
    print('I add ' + pizza_toppings)
    