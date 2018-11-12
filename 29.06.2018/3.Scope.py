class A:
    z=30
    def __init__ (self):
        self.X=2
        self.Y=10
        self.W=100
    def __str__(self):
        return('W:'+str(self.W)+',X:'+str(self.X)+',Y:'+str(self.Y)+'Z:'+str(self.z))
class B(A):
    x=4
    y=20
    def __init__(self):
        A.__init__ (self)
        self.x=6
        self.y=50
    def __str__(self):
        return A.__str__(self)+'V:'+str(self.Y)
def main():
    ob1=A()
    ob2=B()
    print('ob1:\n',str(ob1))
    print('ob2:\n',str(ob2))
    print('Dir(A):\n',dir(A))
    print('Dir(ob1):\n',dir(ob1))
    print('Dir(B):\n',dir(B))
    print('Dir(ob2):\n',dir(ob2))

if __name__ == '__main__':
    main()
