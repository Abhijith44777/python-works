f=open("C:\\Users\\Abhijith\\Desktop\\pythonworks\\hw\\3_word_count","r")

word=[]

for line in f:
  
    line=line.rstrip("\n")
  
    all_word=line.split(" ")
  
    for w in all_word:
  
        word.append(w)
word_count={w:word.count(w) for w in word}
print(max(word_count))