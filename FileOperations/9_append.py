# append-a


f=open("C:\\Users\\Abhijith\\Desktop\\pythonworks\\database\\frame_works.txt","a")

frame_works=["wordpress","springboot","oodo","fastapi"]

for fw in frame_works:
    f.write(fw+"\n")

f.close()