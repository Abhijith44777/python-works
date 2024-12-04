text=["apple","orange","iphone","potato"]

vowels=['a','e','i','o','u']

vowel=[w for w in text if w[0]in vowels]

print(vowel)

consonents=[w for w in text if w[0] not in vowels]

print(consonents)

# longest word

long=max([len(w) for w in text])

print(long)

longest_word=[w for w in text if len(w)==long]

print(longest_word)