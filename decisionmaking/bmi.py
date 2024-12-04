#bmi=weight_in_kg/(height_in_metre)**2

weight_in_kg=int(input("enter weight in kg"))

height_in_kg=int(input("enter weight in cm"))

height_in_metre= height_in_cm/100

bmi=weight_in_kg/(height_in_metre)**2

bmi=round(bmi)

print(bmi)

if bmi<19:  #0-18 range
    print("under weight")

elif bmi<25:  #19-24 #19>=bmi<25
    print("normal weight")

elif bmi<30:  #25-30
    print("overwight")

elif bmi>=30: #>30
    print("obese")             


# print under weight if bmi<19
# print normal weight if bmi 19 to <25
# print normal weight if bmi 25 to <30
# print obese if bmi>=30