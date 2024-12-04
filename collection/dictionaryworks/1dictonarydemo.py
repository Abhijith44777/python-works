# create a dictionary product with keys id,title,price,brand

#key:value

product={"id":25,"title":"bag","price":2500,"brand":"puma"}

print(product["brand"])


#to update a valuee in key(product)

product["brand"]="nike"

print(product)


#to add a line

product["date"]="11-07-2024"

print(product)


#to add a column

product["offer"]="6%"

print(product)


#to check if it exist or not

if "offer" in product:

    print("exist")

else:

    print("not exixt")


#add offer as 10 if offer exist else add offer as 20

if "offer" in product:

    product["offer"]=10

else:

    product["offer"]=20

print(product)    