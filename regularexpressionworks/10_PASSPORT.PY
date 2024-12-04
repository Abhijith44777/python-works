from re import fullmatch
passport_number=input("enter passport number : ")

pattern="[[A-Z][1-9][0-9]\d{4}[1-9]\s?"

matcher=fullmatch(pattern,passport_number)

if matcher==None:
    print("invalid")

else:
    print("valid")    