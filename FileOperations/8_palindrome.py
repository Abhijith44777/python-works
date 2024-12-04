words="C:\\Users\\Abhijith\\Desktop\\pythonworks\\database\\word.txt"
palindrome_words="C:\\Users\\Abhijith\\Desktop\\pythonworks\\database\\palindrome.txt"

word_path=open(words,"r")

palindrome=open(palindrome_words,"w")

for line in word_path:
  
    words=line.rstrip("\n")

    reversed_word=words[::-1]

    if words==reversed_word:
        palindrome.write(words+"\n")

word_path.close()
palindrome.close()        