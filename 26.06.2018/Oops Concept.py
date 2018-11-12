#OOPs concept in python by chetna bajpai <3

class person:
    count=0
    def __init__(self,name,DOB,address):
        self.name=name
        self.DOB=DOB
        self.address=address
        person.count+=1
    def getName(self):
        return(self.name)
    def getAddress(self):
        return(self.address)
    def setName(self,name):
        self.name=name
    def getDOB(self):
        return(self.DOB)
    def setDOB(self,DOB):
        self.DOB=DOB
    def setAddress(self,address):
        self.address=address
    def __str__(self):
        return 'Name: '+self.name+'\nAddress: '+self.address
    def __del__(self):
        print('Deleted')
        person.count-=1
P1=person('Ajay','24-12-80','The Mall-Knp')
P2=person('Ajay','24-12-80','The Mall-Knp')
print(P1.__str__())
print(P2.__str__())

del(P1)
print(P1.__str__())#An error wil be generated bcz P1 is deleted
