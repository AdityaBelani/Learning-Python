#Multilevel Inheritance

class A(object):
    def __init__(self,a):
        self.a=a
        print("Class A Constructor")
    def show(self):
        print("a=", self.a)

class B(A):
    def __init__(self,a,b):
        super(B,self).__init__(a)
        self.b=b
        print("Class b constructor")
    def prin(self):
        print("B=",self.c)

class C(B):
    def __init__ (self,a,b,c):
        B.__init__(self,a,b)
        self.c=c
        print("Class C Constructor")
    def disp(self):
        print("C=",self.c)
        
ob=C(1,2,3)
ob.show()
ob.prin()
ob.disp()
