data = {'a': 20, 'b': 70, 'c': 40, 'd': 80, 'e': 10}


filtered_data = {key: value for key, value in data.items() if value > 50}


print(filtered_data)