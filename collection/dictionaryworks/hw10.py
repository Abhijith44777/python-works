prices = {'apple': 100, 'orange': 50, 'grape': 200, 'carrot': 80}

discount_rate = 0.10

discounted_prices = {item: price * (1 - discount_rate) for item, price in prices.items()}

print(discounted_prices)