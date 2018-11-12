#Running a loop of infinite iterations

def main():
    tot=0
    num=input('Enter a num: ')
    while num!='':
        tot+=int(num)
        num=input('Again enter a num: ')
    print('Sum= ',tot)
if __name__ == '__main__':
    main()
