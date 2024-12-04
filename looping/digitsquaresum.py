number=int(input("enter number:"))

total=0

while(number!=0):

    digit=number%10

    square=digit**2

    total=total+square

    number=number//10

print(total)



