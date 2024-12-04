text="ABBACB"

# print character count

# a:2
# B:3
# C:

character_count={}

for ch in text:
    
    if ch in character_count:
      
        character_count[ch]+=1
    
    else:

        character_count[ch]=1

print(character_count)


# 1st recursive character B

chracter_count={}
for ch in text:
    if ch in character_count:
        print(ch)

        break

    else:
        character_count[ch]=1

