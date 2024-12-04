from re import finditer

text="abbbababbaaabbb"
    # 012345678901234
#pattern="b{2}"#to print letters(b) that are together

pattern="b{1,3}"

pattern="a*"

matcher=finditer(pattern,text)

for obj in matcher:
    print(obj.start(),obj.group())
