def area(l,b):
    a=l*b
    return a

def areasq(s):
    ar=area(s,s)
    return ar

def main():
    print("Enter values for L & B: ")
    L1=int(input('Enter Lenght: '))
    L2=int(input('Enter Breadth: '))
    ar=area(L1,L2)
    print ('Area of Rect:' ,ar)
    ar1=areasq(L1)
    print ('Area od Sq.: ',ar1)

if __name__ == '__main__':
    main()
    print ('End of Prog')
