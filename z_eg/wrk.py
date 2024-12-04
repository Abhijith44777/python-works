# weightinkg=int(input("enter numbet"))
# heightinkg=int(input("enter number"))

# bmi=weightinkg/(heightinkg)**2

# print(bmi)

# if bmi>18:
#     print("underweight")

# elif bmi<25:
#     print("normal")

# elif(bmi<35):
#     print("overweght")    


# centureyr

# year=int(input("enter yr"))

# if year%100==0:
#     print("centure yr")

# else:
#     print("non centure")    

# largest numbr


# num1=int(input("enter number"))
# num2=int(input("enter number"))
# num3=int(input("enter number"))

# if num1>num2 and num1>num3:
#     print("num1 is largest")

# elif num2>num1 and num2>num3:
#     print("num2 is largest")    

# elif num3>num1 and num3>num2:
#     print("num3 is largest")    

# else:
#     print("invild")    

# leapyr

# year=int(input("enter num"))

# if year%4==0 and year%100!=0 or year%400 and year%400:

#     print("leap year")

# else:
#     print("not leap yr")

# def factorial(number):
#     fact=1
    
#     for i in range(1,number+1):
#         fact=fact*i
    
#     return fact 
# result=factorial(3)
# print(result)



# def fact(number):
#     fact=1

#     for i in range(1,number+1):
#         fact=fact*i

#     return fact

# result=factorial(4)            

# print(result)



# def maxnum(num1,num2):
#     return "num1"  if num1>num2 else "num2"

# print(maxnum(200,400))    


# def maxnum(num1,num2):
#     return "num1" if num1>num2 else "num2"

# print(maxnum(380,244))    

# def perfectnumber(number):
#     for i in range(1,number+1):
#         return "perfect number" if number%i==0 else "not perfect number"
# print(perfectnumber(567))        

# def prime_number(number):
#     for i in range(2,number):
#         return "prime number" if number%i==0 else "not prime numeber" 

# print(prime_number(25))        

# sequence=range(1,11,1)
# for i in sequence:
#     print(i)


# sequence=range(1,11,-1)

# for i in sequence:
#     print(i)


# armstrong


# number=int(input(("enter number")))

# orginal=number

# digit_count=len(str(number))

# total=0

# while(number!=0):

#     digit=number%10

#     exponent=digit**digit_count

#     total=total+exponent

#     number=number//10

# print("armstrong number" if total==orginal else "not armstrong"   )


lst=[10,33,22,19,30]
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)