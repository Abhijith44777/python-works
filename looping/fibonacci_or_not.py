number=int(input("enter number : "))

previous=0

current=1

is_fibonacci=False

for i  in range(1,number+1):
    
    next=previous+current

    previous=current

    current=next
    
    if next==number:

        is_fibonacci=True
        
        break
    
    print(is_fibonacci)