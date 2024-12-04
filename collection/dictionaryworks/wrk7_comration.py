arr=[10,20,30,40,2,3]

#even numbers

result={num:num**3 for num in arr if num%2==0}

print(result)


#odd numbers


result={num:num**3 for num in arr if num%2!=0}

print(result)

