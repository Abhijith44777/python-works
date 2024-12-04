def perfect_number(number):
    for i in range(1,number):
        return "perfect_number" if number%i==0 else "not perfect_number"

print(perfect_number(7))        
        