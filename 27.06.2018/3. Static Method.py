#Static Method

class person:
    PersonCount=0
    def __init__ (self,name,DOB,address):
        self.name=name
        self.DOB=DOB
        self.address=address
        person.incPersonCount()
    @staticmethod #Means this method is static
    def incPersonCount():
        person.PersonCount+=1
    @staticmethod
    def getPersonCount():
        print(person.PersonCount)
P1=person('Ravi','20-June-1980','House No.17-Block 10 , Delhi')
P2=person('Ravi','20-June-1980','House No.17-Block 10 , Delhi')
person.getPersonCount() #2
