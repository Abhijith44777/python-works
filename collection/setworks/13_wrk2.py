text="this is a text to remove dupliate words this is simple"


#split text

words=text.split(" ")

print(set(words))

text2="this simple text remove duplicate words"

words2=text2.split(" ")

issubset=set(words2).issubset(set(words))

print(set(words))

print(issubset)