from re import fullmatch

user_input=input("enter variable name : ")

# variable name must start with an alphabets(lowercase or uppercase)
# any number of alphabets,digits,_

pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("invalid")

else:
    print("valid")    