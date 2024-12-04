class GrandParent:
    def m1(self):
        print("Grand parent class m1 method")

class parent():
    def m2(self):
        print("parent class m2 method")
class child(parent,GrandParent):
    def m3(self):
        print("child class m3 methd")
                                      
child_instane=child()
child_instane.m3()
child_instane.m2()
child_instane.m1()


# if m in grandparant and  m in  parent  child (parent,grandparent)
# in which m in  parent work first if  m not in parent  grandparent work
class GrandParent:
    def m(self):
        print("Grand parent class m1 method")

class parent():
    def m(self):
        print("parent class m2 method")
class child(parent,GrandParent):
    def m3(self):
        print("child class m3 method")
                                    
child_instane=child()
child_instane.m3()
child_instane.m()