fruits = ['apple', 'banana', 'orange']

prices = [199, 99, 249]

fruit_prices = {fruits[i]: prices[i] for i in range(len(fruits))}

print(fruit_prices)