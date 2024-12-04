def student_info(*args,**kwargs):

    if kwargs.get("operation")=="total":
        return sum(args)

    if kwargs.get("operation")=="avg":
        return sum(args)/len(args)

print(student_info(57,87,97,operation="avg"))    

print(student_info(55,88,77,operation="total"))