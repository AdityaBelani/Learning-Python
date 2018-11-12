import sys
sys.path.append('')
import nestedfunc
def main():
    print ('Enter values for floor: ')
    Length=int(input('Length: '))
    Breadth=int(input('Breadth: '))
    print(nestedfunc.area(Length,Breadth))
if __name__ == '__main__':
    main()
