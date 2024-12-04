weight_in_kg=int(input("enter weight in kg :"))

height_in_cm=int(input("enter height in cm :"))

height_in_metre=height_in_cm/100

BMI=weight_in_kg/(height_in_metre)**2

BMI-round (BMI, 2)

print(BMI)

if BMI<19:
    print("underweight")

elif BMI>=19 and BMI<25:
    print("normal weight")

elif BMI>=25 and BMI<30:
    
    print("over weight")

elif BMI>=30:
    print("obese")

else:
    print("invaild")