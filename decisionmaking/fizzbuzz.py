num=int(input("enter number:"))

if num%3==0:
    print("fizz")

elif num%5==0:
    print("buzz")

elif num%15==0:
    print("fizzbuzz")

else:
    print("invalid number")            