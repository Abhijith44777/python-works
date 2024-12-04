#list comprehension


#reference=[return itereatuin condition]

arr=[2,3,4,5,6,7]

square=[num**2 for num in arr]

print(square)




# mapping=no condition
# filter=has condition
# reduce



#even number
arr=[2,3,4,5,6,7]
even_num=[num for num in arr if num%2==0]

print(even_num)

#odd number

odd_num=[num for num in arr if num%2!=0]

print(odd_num)

#greater than 5

num_greaterthan_five=[ num for num in  arr if num>5]

print(num_greaterthan_five)