# text="pneumonoultramicroscopicsilicovolcanoconiosis"

# v_count=0

# c_count=0

# text=text.casefold()
# for ch in text:

#     if ch=="a" or ch=="e" or ch=="i" or ch=="u" :

#         v_count=v_count+1

#     else:

#         c_count+=1

#     print("vowel count =",v_count)

#     print("consonent count =",c_count)

text="pneumonoultramicroscopicsilicovolcanoconiosis"

v_count=0
c_count=0
text=text.casefold()

for ch in text:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        v_count=v_count+1
    else:
        c_count=c_count+1

    print("vowel_count =", v_count) 

    print("consnent count =",c_count)       