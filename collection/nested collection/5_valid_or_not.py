# sample_input="{}"
# op=>valid

# sample_input="{()}"
# op=>valid

# sample_input="{(})"
# op=>invalid

# sample_input="[]("
# op=>invalid

ueser_input=input("enter brackets pairs")

symbol_dictionary={
    "{":"}",
    "[":"]",
    "(":")",
    "<":">"
}

symbol_stack=[]

top=-1

is_valid=True

for symbol in ueser_input:

    if symbol in symbol_dictionary:#symbol is an opening

        top=top+1
        
        symbol_stack.append(symbol)#push the symbol to stack

    elif top==-1:
        
        is_valid=False

    elif symbol==symbol_dictionary.get(symbol_stack[top]):#chk symbol is a valid closing

        top=top-1

        symbol_stack.pop()

    else:

        is_valid=False

if len(symbol_stack)==0 and is_valid==True:

    print("valid")

else:
    print("invalid")    