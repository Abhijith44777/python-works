#Write a Python program that reads an integer from the user and performs the

#following checks:

#1.If the number is divisible by 3, print "PING".

#2.If the number is divisible by 5, print "PONG".

#3.If the number is divisible by 15, print "PINGPONG".

#4.If the number is not divisible by 3 or 5, print the number itself.

number=int(input("enter the number : "))

if number%3==0:
    print("PING")

elif number%5==0:
    print("PONG")

elif number%15==0:
    print("PINGPONG")

else:
    print("number")