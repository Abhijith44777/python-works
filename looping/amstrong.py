#digit count

number=int(input("enter number:"))

orginal=number

digit_count=len(str(number))       #len(obj)  => return length of object,that's not must be int

total=0

while(number!=0):

    digit=number%10

    exponent=digit**digit_count

    total=total+exponent

    number=number//10

print("armstrong number" if total==orginal else "not armstrong number" )