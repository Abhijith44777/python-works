num1=int(input("enter num1 : "))
num2=int(input("enter num2 : "))

try:
    result=num1/num2
    print(result)

# except:
#     print("error")    


except Exception as e:
    print(e)    

print("file write")

print("database")