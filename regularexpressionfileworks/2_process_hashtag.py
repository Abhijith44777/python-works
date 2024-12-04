from re import finditer

f=open("C:\\Users\\Abhijith\\Desktop\\pythonworks\\regularexpressionfileworks\\2_hashtag.txt")

for line in f:
    
    hashtag=line.rstrip("\n")
    
    pattern="#\w+"
    
    matcher=finditer(pattern,hashtag)

    for obj in matcher:

        print(obj.group())
