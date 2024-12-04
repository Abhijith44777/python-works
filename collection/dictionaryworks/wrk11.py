lst1=["apple","mango","onion","potatto"]
lst2=[100,200]
# {"apple":100,"mango":200:,"onion":1,"potatto":2}

# products={key:value for key,value in zip(lst1,lst2)}

# print(products)

result={}
for i in range(0,len(lst2)):
    list_one_index_element=lst1[i]
    list_two_index_element=lst2[i]

    result[list_one_index_element]=list_two_index_element
balance_elements=lst1[len(lst2):]
for index,element in enumerate(balance_elements):
    result[element]=index+1
print(result)    