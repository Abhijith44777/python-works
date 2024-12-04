f1=open("C:\\Users\\Abhijith\\Desktop\\pythonworks\\database\\all_students.txt","r")
f2=open("C:\\Users\\Abhijith\\Desktop\\pythonworks\\database\\failed_students.txt","r")
all_students_sets=set()
failed_students_sets=set()
for line in f1:
    line=line.rstrip("\n")
    all_students_sets.add(line)
for line in f2:
    line=line.rstrip("\n")
    failed_students_sets.add(line)
passed_students=all_students_sets.difference(failed_students_sets)
print(passed_students)