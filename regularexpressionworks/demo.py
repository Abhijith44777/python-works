def smart_function(num1, num2):
    assert num1>0, "num1 should be > 0"
    assert num2>0, "num2 should be > 0"
    yield num1-num2
    yield num1/num2

generator_objects=smart_function(10,0)

for result in generator_objects:
    print(result)