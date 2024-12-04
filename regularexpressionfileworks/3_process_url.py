from re import findall

f=open("C:\\Users\\Abhijith\\Desktop\\pythonworks\\regularexpressionfileworks\\3_url.txt")

content=f.read()

pattern="https?://[\w+\S./]+"

urls=findall(pattern,content)

for urls in urls:

    print(urls)

