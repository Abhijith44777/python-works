f=open("C:\\Users\\Abhijith\\Desktop\\pythonworks\\database\\names.txt","w")

languages=["python","java","c#","javascript"]

for l in languages:
    f.write(l+"\n")

f.close()