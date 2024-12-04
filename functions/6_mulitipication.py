# create a fn multiplication_table(number,n)
# print multiplication_table of number till n

def multiplication_table(num,n):

    for i in  range (1,n+1):
        print(f"{i} * {num} = {i*num}")

print(multiplication_table(3,50))
