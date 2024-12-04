from re import findall

f=open("C:\\Users\\Abhijith\\Desktop\\pythonworks\\regularexpressionfileworks\\4_data.txt")

content=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

dates=findall(pattern,content)

for date in dates:
    
    print(date)