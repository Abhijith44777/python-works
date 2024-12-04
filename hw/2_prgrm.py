f=open("C:\\Users\\Abhijith\\Desktop\\pythonworks\\hw\\user.txt","a")

user_details=["contact_number","address","salary"]

for i in user_details:
    f.write(i+"\n")

f.close()    