
# arr=[2,3,4,5]

# sum=int(input("enter number : "))

# for i in range(0,len(arr)-1):

#     for j in range(i+1,len(arr)):

#         current_sum=arr[i]+arr[j]
        
#         if sum==current_sum:

#             print(arr[i],arr[j])

#             break


arr=[2,3,4,5,6,7,8,9]

left=0

right=len(arr)-1

sum=12

while left<right:
    
    current_sum=arr[left]+arr[right]

    if current_sum==sum:
        print(arr[left],arr[right])

        break

    elif current_sum>sum:

        right=right-1

    elif current_sum<sum:

        left=left+1    