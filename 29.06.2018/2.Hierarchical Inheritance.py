class A(object):
    def __init__(self,a):
        self.a=a
        print('Class A Constructor')
    def show(self):
        print('a= ',self.a)
class B(A):
    def __init__ (self,a,b):
        super(B,self). __init__(a)
        self.b=b
        print('Class B Constructor')
    def disp(self):
        print('b= ',self.b)
class C(A):
    def __init__(self,a,c):
        A.__init__(self,a)
        self.c=c
        print('Class C Constructor')
    def disp(self):
        print('C= ',self.c)
ob=B(12,22)
ob.show()
ob.disp()
oc=C(11,23)
oc.show()
oc.disp()
