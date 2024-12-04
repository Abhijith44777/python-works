arr=[10,20,30
,]
arr=[20,21,10,14,13,12]

arr1.sort()
arr2.sort()

p1=0

p2=0

while(p1<len(arr1) or p2<len(arr2)):

    if arr1[p1]==arr[p2]:

        print(arr1[p1])

        p1+=1

        p2+=1