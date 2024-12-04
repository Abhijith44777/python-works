def sort_num(*args,**kwargs):
    if kwargs.get("reverse")=="True":
        return sorted(args,reverse=True)

    if kwargs.get("reverse")=="False":
        return sorted(args)




print(sort_num(7,57,33,2,5,56,reverse="True"))        

print(sort_num(7,57,33,2,5,56,reverse="False"))        