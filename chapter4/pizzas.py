pizzas = ['peperoni', 'margorita', 'chesari', 'nikocia']
friend_pizzas = pizzas[:]
pizzas.append('sicili')
friend_pizzas.append('lanita')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
