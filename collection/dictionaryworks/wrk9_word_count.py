text="ABABBCCDDE"

character_frequency={ch:text.count(ch) for ch in text}

print(character_frequency)


# print non recursive elements


for k,v in character_frequency.items():
    if v==1:
        print(k)


# another method

non_recursive_character=[k for k,v in character_frequency.items() if v==1]        

print(non_recursive_character)