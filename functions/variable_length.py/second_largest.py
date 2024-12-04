# create a fn that accept any arguments and return second max number


def second_max_num(*args):
    
    sorted_num=sorted(args,reverse=True)

    return sorted_num[1]

print(second_max_num(10,20,30,40))    
print(second_max_num(39,49,59,23,55,677))