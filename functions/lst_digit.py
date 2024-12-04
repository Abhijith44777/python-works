def last_digit_max(num1,num2):
    
    num1_last_digit=num1%10
    
    num2_last_digit=num2%10

    print(num1 if num1_last_digit>num2_last_digit else num2)

last_digit_max(123,871)





