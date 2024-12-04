f=open("C:\\Users\\Abhijith\\Desktop\\pythonworks\\database\\questions.txt","r")

word=[]

for line in f:
  
    line=line.rstrip("\n")
  
    all_word=line.split(" ")
  
    for w in all_word:
  
        word.append(w)
word_count={w:word.count(w) for w in word}

sorted_word_count=sorted(word_count,key=lambda k:word_count.get(k),reverse=True)


value_key=[[v,k]for k,v in word_count.items()]

print(sorted(value_key,key=lambda lst:lst[0],reverse=True))