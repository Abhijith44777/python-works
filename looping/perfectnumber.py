# write a program to check the number is perfect or not

num=int(input("enter number: "))

total=0

for i in range(1,num):

    if num%i==0:
        total+=i

print("perfect" if total==num else "not perfect number")