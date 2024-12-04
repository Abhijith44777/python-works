from re import fullmatch

number_input=input("enter number :")

pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"
matcher=fullmatch(pattern,number_input)

if matcher==None:
    print("invalid")

else:
    print("valid")    