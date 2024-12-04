arr=[10,20,30,40,2,3]
#{10:100,20:400......}


result={}

for num in arr:
    square=num**2
    result[num]=square
print(result)

#square comration

arr=[10,20,30,40,2,3]

# result={key:value itretion condition}

result={num:num**2 for num in arr}

print(result)

