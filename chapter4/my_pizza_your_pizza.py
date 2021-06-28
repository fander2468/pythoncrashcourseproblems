favorite_pizzas = ['sausage', 'pepperoni', 'cheese']

for favorite_pizza in favorite_pizzas:
    print('I like', favorite_pizza, 'pizza.')
print('As you can see, I really love pizza!')

friends_pizzas = favorite_pizzas[:]
favorite_pizzas.append('mushroom')
friends_pizzas.append('anchovies')

print('My Favorite pizzas are:', favorite_pizzas)
print("My friends favorite pizzas are:", friends_pizzas)