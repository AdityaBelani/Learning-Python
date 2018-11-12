def insertionsort(lst):
    for i in range(1,len(lst)):
        temp=lst[i]
        j=i-1
        while j>=0 and lst[j]>temp:
            lst[j+1]=lst[j]
            j=j-1
        lst[j+1]=temp

def main():
    lst=list(input('Enter a List: '))
    print('The sorted List: ')
    insertionsort(lst)
    print(lst)

if __name__ == '__main__':
    main()
