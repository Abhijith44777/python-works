words=["hello","hai","hello","this","is","this","is","hello"]

word_frequency={w:words.count(w) for w in words}

print(word_frequency)

# recursive=repeated

recursive_words=[k for k,v in word_frequency.items() if v>1]

print(recursive_words)

# non recursive words

non_recursive_words=[k for k,v in word_frequency.items() if v==1]

print(non_recursive_words)

# most recursive word

most_recursive_word[k for k,v in word.items() if v=]

print(most_recursive_word)