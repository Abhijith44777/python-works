arr=[[10,20],
    [20,30],
    [30,40],
    [40,50]]

flat_lst=[num for lst in arr for num in lst]

print(flat_lst)

gtr_25=[num for lst in arr for num in lst if num>25]
print(gtr_25)