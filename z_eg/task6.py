array= ["flight", "flow", "flash"]

small =min(array)

large =max(array)

common_prefix =""

for i, char in enumerate(small):
    if char==large[i]:
        common_prefix += char

    else:
        break

print(common_prefix)