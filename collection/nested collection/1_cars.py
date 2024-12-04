cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt"]},
]

# print count of vechicles

print(f"total vechicles=> {len(cars)}")


# print available colors of baleno

available_colors=[c.get("colors") for c in cars if c.get("name")=="baleno"]         #******list comprehencion******


print(available_colors[0])       

# print all brand

all_brand={c.get("brand")for c in cars}     #******set comprehencion******

print(all_brand)

# print cars name available in amt transmissions


cars_name=[c.get("name") for c in cars if "amt" in c.get("transmissions")]

print(cars_name)

# cars in blue colors

blue_cars=[c.get("name") for c in cars if "blue" in c.get("colors")]

print(blue_cars)


# print all transmissions

all_transmissions={t for c in cars for t in c.get("transmissions")}
print(all_transmissions)

# print all colors

all_colors={colors for c in cars for colors in c.get("colors")}

print(all_colors)

# most popular colors



all_clr=[clr for c in cars for clr in c.get("colors")]
grp={clr:all_clr.count(clr) for clr in all_clr}
print(max(grp))

#costly car
# costly_car={c.get("name"):c.get("price") for c in cars }
# print(max(costly_car))

costly_car=max(cars,key=lambda d:d.get("price"))

print(costly_car.get("name"))

#car with minimum cost

print(min(costly_car))

#sort cars with price

sorted_car=sorted(cars,key=lambda d:d.get("price"),reverse=True)

sorted_car_name=[c.get("name")for c in sorted_car]

sorted_car_name_price={c.get("name"):c.get("price")for c in sorted_car}
sorted_car_name_price_brand={c.get("name"):[c.get("price"),c.get("brand")]for c in sorted_car}
print(sorted_car_name)

print(sorted_car_name_price)

print(sorted_car_name_price_brand)