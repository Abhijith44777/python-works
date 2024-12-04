from json import load

f=open("C:\\Users\\Abhijith\\Desktop\\pythonworks\\database\\employee.json")

data=load(f)

for emp in data:

    print(emp) 