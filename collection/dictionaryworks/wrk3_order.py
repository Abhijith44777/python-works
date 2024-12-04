order=["tea","cofee","gheerost","plainrost","porotta","tea"]

order_summery={}

for w in order:
    if w in order_summery:
        order_summery[w]+=1

    else:
        order_summery[w]=1

print(order_summery)            