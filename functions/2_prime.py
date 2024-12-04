def check_prime(number):
    
    is_prime=True

    if number==2:

        is_prime=True


    else:
        for i in range(2,number):
            if number%i==0:
                is_prime=False

                break

    return is_prime

print(check_prime(2))

