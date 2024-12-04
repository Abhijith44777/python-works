
#*******lambda functions*********



#to add two numbers
add=lambda n1,n2:n1+n2

print(add(10,5))


# to sub two numbers
sub=lambda n1,n2:n1-n2

print(sub(29,19))

#to find cube of a number

cube=lambda n:n**3

print(cube(5))


# to take max length of string

max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2

print(max_two("apple","orange"))

#min two numberrs


min_two=lambda str1,str2:str1 if len(str1)<len(str2) else str2

print(min_two("apple","orange"))

#smart sub

smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1

print(smart_sub(29,200))


words=["hello","hai","morning","test","apple"]

def get_length(words):

    return len(words)

print(max(words,key=get_length))    



#or

get_length=lambda word:len(word)

print(max(words,key=get_length))



#to get the max length words


text="this is a simple programing question to find the word with maximum number of characters"

#step 1 split the text into words

words=text.split(" ")

def get_length(w):

    return len(w)

print(max(words,key=get_length))


# sorted order


words=text.split(" ")

def get_length(w):

    return len(w)

str_words=sorted(words,key=get_length,reverse=True)

print(str_words)

#most recursive words
words=text.split(" ")

def get_count(w):

    return words.count(w)

frequent_word=max(words,key=get_count)

print(frequent_word)



#QN:2

text="ABAABBC"

#most recursive character



def get_count(ch):

    return text.count(ch)
most_frequent_character=max(text,key=get_count)    

print(most_frequent_character)


least_frequent_character=min(text,key=get_count)    
print(least_frequent_character)





#non recursive character