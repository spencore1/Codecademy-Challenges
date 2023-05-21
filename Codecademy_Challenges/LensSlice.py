toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)

print('We sell', num_pizzas, 'different kinds of pizza!')

pizza_and_prices = [[2, 'Pepperoni'], [6, 'Pineapple'], [1, 'Cheese'], [3, 'Sausage'], [2, 'Olives'], [7, 'Anchovies'], [2, 'Mushrooms']]
print(pizza_and_prices)

pizza_and_prices.sort()
print(pizza_and_prices)