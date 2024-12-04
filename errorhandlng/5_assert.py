def poll(age):
    assert age >18,"invalid age"

    print("voted")
# poll(11)
try:
    poll(13)

except Exception as e:
    print(e)



    

def review(rating):
    assert rating>0,"too low"

    assert rating in range(0,11),"too high"

print("rated")