# create a dictionary employee with keys eid,name,salary,department,experience


employee={"eid":201,"name":"abhijith","salary":100000,"departmant":"texting","experience":2}

print(employee["experience"])

#add contact number of employee

employee["contact"]=9447771310

print(employee)


# if experience>5 update employee salary as current salary+20000 else current salary+15000

if employee["experience"]>5:
    employee["salary"]+=20000

else:

    employee["salary"]+=15000

print(employee)    


#add a role SDE if exp>5 else add JDE

if employee["experience"]>5:

    employee["role"]="SDE"
else:
    employee["role"]="JDE"    

print(employee)
