
def swap_dec(fn):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)

    return wrapper

def round_dec(fn):
    def wrapper(n1,n2):
        n1=round(n1)
        n2=round(n2)
        return fn(n1,n2)
    return wrapper

@round_dec       
@swap_dec
def add_number(num1,num2):
    return num1+num2

@round_dec
@swap_dec
def substration(num1,num2):
    return num1-num2

@round_dec
@swap_dec
def division(num1,num2):
    return num1/num2    

# print(division(10,2))    
# print(division(2,10))
# print(substration(7,88))

print(substration(8.9,88.2))
print(division(5.7,36.2))