from re import fullmatch

number_input=input("enter mobile number :")

pattern="(91)?[0-9]{10}"

matcher=fullmatch(pattern,number_input)

if matcher==None:
    print("invalid")

else:
    print("valid")    