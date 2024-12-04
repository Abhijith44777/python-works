from re import fullmatch
dob=input("enter date : ")

pattern="([1-9]|0[1-9]|1[0-9]2[0-9]|3[01])"  #day
        # "(0?[1-9]|[12][0-9|3[01])"
      
matcher=fullmatch(pattern,dob)

if matcher==None:
    print("invalid")

else:
    print("valid")    