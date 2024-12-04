from re import fullmatch

number_input=input("enter number : ")

pattern="[2-9]{1}[0-9]{3}\s[0-9]{4}[0-9]{4}"

matcher=fullmatch(pattern,number_input)

if matcher==None:
    print("invalid")

else:
    print("valid")    