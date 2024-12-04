f=open("C:\\Users\\Abhijith\\Desktop\\pythonworks\\database\\fruits.txt","r")

fruits=[]

for line in f:

    fruits.append(line.rstrip("\n"))

print(fruits)    