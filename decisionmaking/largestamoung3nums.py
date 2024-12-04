num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))

if num1>num2 and num1>num3:
    print("num1 is the largest")

elif num1<num2 and num2>num3:
    print("num2 is the largest")

elif num1<num3 and num2<num3:
    print("num3 is the largest") 

elif num1==num2 and num1==num3:
    print("three numbers are equal")    

else:
    print("invalid")            