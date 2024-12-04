source_word="CHICKEN"
target_word="HENZ"

#kangaroo word
# character_count={}

# for ch in source_word:
#     if ch  in character_count:
   
#         character_count[ch]+=1

#     else:
#         character_count[ch]=1
    
character_count={ch:source_word.count(ch) for ch in source_word }

is_kangaroo=True

for ch in target_word:

    if ch in character_count and character_count.get(ch)>0:

        character_count[ch]-=1

    else:

        is_kangaroo=False
        break
# character_count={ch:source_word(ch) for ch in source_word}
print(is_kangaroo)
