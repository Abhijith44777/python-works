def calculator(*args,**kwargs):
    if kwargs.get("operation")=="+":
        return sum(args)

    if kwargs.get("operation")=="*":
        result=1

        for num in args:

            result=result*num
        return result

print(calculator(29,49,50,operation="+"))              

print(calculator(567,7,operation="*"))