class person:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    
    def display_person_info(self):
        print(self.name,self.age)

class employee:
    def _init_(self,eid,salary):
        self.eid=eid
        self.salary=salary

    def display_employee_info(self):
        print(self.eid,self.salary)

class manager(person,employee):
    department:str
    def _init_(self,age,name,eid,salary,department):
        person._init_(self,age,name)
        employee._init_(self,eid,salary)
        self.department=department
    
    def display_manager_info(self):
        self.display_person_info()
        self.display_employee_info()
        print(self.department)

manager_instance=manager(32,"hari","eol",54000,"hr")
manager_instance.display_manager_info()