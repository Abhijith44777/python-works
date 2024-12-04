begin=int(input("enter starting limit:"))
end=int(input("enter limit:"))

if begin>end:
    begin,end=end,begin

i=begin    

while(i<=end):
    if i%2==0:
      
        print(i)

    i=i+1