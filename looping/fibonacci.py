previous=0

current=1

print(previous)

print(current)

for i in range(1,8):
    
    next=previous+current
    
    print(next)
    
    previous=current
    
    current=next


