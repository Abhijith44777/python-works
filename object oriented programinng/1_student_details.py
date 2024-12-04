

# set_student()

# display_student() 

class Student:
    name:str

    rolnumber:int

    age:int

    course:str

# initializing attributes of Student class

    def set_student(self, name, rolnumber, age, course):
        
        self.name=name

        self.rolnumber=rolnumber

        self.age=age

        self.course=course

    def display(self):
        
        print(self.name, self.age, self.rolnumber, self.course)

# refence_name=ClassName()

student_instance1=Student()


student_instance1.set_student("vyshnav", 100, 35, "django")

student_instance1.display()




# *******constructor*******

# python == __init__   calls automatically,

# java == ClassName