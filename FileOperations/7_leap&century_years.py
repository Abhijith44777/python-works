years_path="C:\\Users\\Abhijith\\Desktop\\pythonworks\\database\\years.txt"
century_year_path="C:\\Users\\Abhijith\\Desktop\\pythonworks\\database\\century_years.txt"
leap_year_path="C:\\Users\\Abhijith\\Desktop\\pythonworks\\database\\leap_year.txt"


f_read=open(years_path,"r")
f_century=open(century_year_path,"w")
f_leapyear=open(leap_year_path,"w")

for year in f_read:

    year=int(year)

    if year%100==0:
        f_century.write(str(year)+"\n")

    if year%100==0 and year%400==0 or year!=0 and year%4==0:

        f_leapyear.write(str(year)+"\n")

f_read.close()

f_century.close()

f_leapyear.close()