class ParentClass(object):
    def __init__ (self,name,regno):
        self.name=name
        self.regno=regno

class DerivedClass(ParentClass):
    def __init__ (self,name,regno,favsub):
        ParentClass.__init__(self,name,regno)
        self.favsub=favsub
    def show(self):
        print('Name: ',self.name)
        print('RegNo.: ',self.regno)
        print('Favourite Subject: ',self.favsub)
    

obj=DerivedClass('Aditya',504,'Computers')
obj.show()
