from re import fullmatch
dob=input("enter month : ")

pattern="([0-9]|0[1-9]|1[0-2])"

matcher=fullmatch(pattern,dob)

if matcher==None:
    print("invalid")

else:
    print("valid")    