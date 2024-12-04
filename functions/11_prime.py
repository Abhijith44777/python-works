def prime_number(number):
    
    for i in range(2,number):
        
        return "prime_number" if number%i==0 else not "prime_number"

print(prime_number(25))