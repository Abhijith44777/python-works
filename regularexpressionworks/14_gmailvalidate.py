from re import fullmatch
mail=input("enter gmail id : ")

pattern="[a-z]+[a-z0-9]{5,63}@gmail.com"
        
matcher=fullmatch(pattern,mail)

if matcher==None:
    print("invalid")

else:
    print("valid")    