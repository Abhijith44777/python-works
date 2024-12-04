from json import load

f=open("C:\\Users\\Abhijith\\Desktop\\pythonworks\\database\\countries.json",encoding="utf-8")

data=load(f)

# print number of countries

# print(len(data))

all_country_names=[country.get("name") for country in data]

# print(all_country_names)

# print all regions

all_region=[country.get("region") for country in data ]

# print(set(all_region))

# to printregion count

region_count={region:all_region.count(region) for region in all_region}

# print(region_count)

max_region_count=max(region_count,key=lambda k:region_count.get(k))
# print(max_region_count,region_count.get(max_region_count))


# capital of a specific country

# specific_capital=input("enter country : ")
# country_capital=[country.get("capital")for country in data if country.get("name")==specific_capital]
 # print(country_capital)


# capital of india

country_capital=[country.get("capital")for country in data if country.get("name")=="India"]
# print(country_capital)


# countries with most number of boarders

country_border={country.get("name"):len(country.get("borders",[]))for country in data}
# print(country_border)

max_border_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

# print(max_border_country)


# most population country

most_population_country=max(data,key=lambda country:country.get("population",0)).get("name")
# print(most_population_country)


# countries that shares boarders with india 
alfa_three_code=[country.get("borders") for country in data if country.get("name")=="India"][0]

for code in alfa_three_code:
  
    for country in data:
  
        if country.get("alpha3Code")==code:
  
            print(country.get("name"))