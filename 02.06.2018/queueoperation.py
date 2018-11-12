from queue import Queue
def main():
    while 1:
        print('Choose an option\n')
        print('1. Create Queue')
        print('2. Delete Queue')
        print('3. Enque')
        print('4. Deque')
        print('5. Print Queue Data')
        print('6. Front Element')
        print('7. No. of Elements')
        choice=int(input('Your choice: '))
        if choice==1:
            q=Queue()
            print('Queue Created')
        elif choice==2:
            del q
            print('Queue Deleted')
        elif choice==3:
            element=int(input('Enter Element to insert'))
            q.enque(element)
        elif choice==4:
            print('Element Deleted: ',q.deque())
        elif choice==5:
            print(q)
        elif choice==6:
            print('Front Element: ',q.Front())
        elif choice==7:
            print('Size= ',q.size())
        proceed=input('Enter y to proceed: ')
main()
