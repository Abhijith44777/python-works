def product(number):
    n = len(number)
    result = [1] * n
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= number[i]
        right_product = 1

        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= number[i]
        return result

number1 = [1, 2, 3, 4]
number2 = [-1, 1, 0, -3, 3]
print(product(number1)) 
print(product(number2))