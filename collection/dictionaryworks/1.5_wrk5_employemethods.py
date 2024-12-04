# employee id,name,department,age,salary

employee={"id":101,"name":"abhijith","department":"developer","age":22,"salary":10000}

#get
print(employee.get("department"))#get key-if invalid it returns "none"

#pop

employee.pop("salary")#pop is used to remove an item

print(employee)

#for taking keys


for k in employee.keys():

    print(k)

#for taking values    

for v in employee.values():

    print(v)    

# for taking  key and values put items eg:employee.items

for k,v in employee.items():

    print(k,v)    
    