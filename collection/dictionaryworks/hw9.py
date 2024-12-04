data = {'a': -20, 'b': 50, 'c': 40, 'd': 80, 'e': -30}

absolute_data = {key: abs(value) for key, value in data.items()}

print(absolute_data)