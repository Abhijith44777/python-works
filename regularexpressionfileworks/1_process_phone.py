
from re import fullmatch

f=open("C:\\Users\\Abhijith\\Desktop\\pythonworks\\regularexpressionfileworks\\phone_no.txt")

for line in f:
    phone=line.rstrip("\n")

    pattern="(91)?[0-9]{10}"

    matcher=fullmatch(pattern,phone)

    if matcher!=None:

        print(phone)    
