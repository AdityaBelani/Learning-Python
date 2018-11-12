from stack import stack
def main():
    while 1:
        print('Choose an option:\n')
        print('1. Create Stack')
        print('2. Delete Stack')
        print('3. Push')
        print('4. Pop')
        print('5. Print Stack Data')
        print('6. Top Element')
        print('7. No. of Element')
        choice=int(input('Enter your choice: '))
        if choice==1:
            stk=stack()
            print('Stack Created...')
        elif choice==2:
            del stk
            print('Stack Deleted...')
        elif choice==3:
            element=int(input('Enter the no. to be inserted...'))
            stk.push(element)
        elif choice==4:
            print('Element Poped=',stk.pop())
        elif choice==5:
            print(stk)
        elif choice==6:
            print('Top element:', stk.top())
        elif choice==7:
            print('Size= ',stk.size())

        proceed=input('Enter y to proceed: ')
        if proceed!='y':
            break
main()
