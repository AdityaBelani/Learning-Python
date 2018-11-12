#Multiple Inheritance: Where one sub class inherits 2 or more sub classes.

class student(object):
    def __init__ (self,ID,name):
        self.ID=ID
        self.name=name
    def show(self):
        print('Student Name: ',self.name)
        print('Student ID: ',self.ID)

class teacher(object):
    def __init__ (self,tec_id,tec_name,subject):
        self.tec_id=tec_id
        self.tec_name=tec_name
        self.subject=subject
    def disp(self):
        print('Teacher Name: ',self.tec_name)
        print('Teacher Id: ',self.tec_id)
        print('Teacher sub: ',self.subject)

class school(student,teacher):
    def __init__(self,ID,name,tec_id,tec_name,subject,sch_id):
        student.__init__(self,ID,name)
        teacher.__init__(self,tec_id,tec_name,subject)
        self.sch_id=sch_id
    def display(self):
        print('School ID: ',self.sch_id)
s1=school(101,'S.N. Singh',101,'XYZ','Python Prog',1001)
s1.show()
s1.disp()
s1.display()
