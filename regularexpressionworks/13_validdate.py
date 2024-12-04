# validate years 1800-2024

from re import fullmatch
date=input("enter date : ")

pattern="(18)[0-9]{2}|(19)[0-9]{2}|(20)[01][0-9]|(202)[0-4]"
        # "((18|19))" 
matcher=fullmatch(pattern,date)

if matcher==None:
    print("invalid")

else:
    print("valid")    