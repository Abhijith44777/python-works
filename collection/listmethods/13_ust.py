arr=[10,20,30,40,50,60]
#     0 , 1 , 2 , 3 , 4 , 5 , 6  ,7


odd=[arr[i] for i in range(1,len(arr),2)]

odd.reverse()

j=0

for i in range(1,len(arr),2):

   arr[i]=odd[j]
   j+=1

print(arr)    




# print(odd_position_elements)

# for i in range(1,len(arr),2):



