from re import finditer

text=" I have 3 cars,2 bikes and 1-cycle "

# pattern="\w" #[a-zA-Z0-9] alphanumeric

# pattern="\d" #"[0-9]"

#pattern="\D" #"[^0-9]"exclude digits

#pattern="\W" #special characters [^a-zA-Z0-9]

pattern="\s" #getting space

pattern="\S"  #excluding space

matcher=finditer(pattern,text)

for obj in matcher:
    print(obj.start(),obj.group())