# to print years -1800-2024


f=open("C:\\Users\\Abhijith\\Desktop\\pythonworks\\database\\years.txt","w")

for years in range(1800,2025):

    f.write(str(years)+"\n")

f.close()    