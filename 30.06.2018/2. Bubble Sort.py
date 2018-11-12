def bubsort(lst):
    for i in range(0,len(lst)-1):
        for j in range(0,len(lst)-1):
            if lst[j]>=lst[j+1]:
                t=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=t
#    print('The new List')
#    print(lst)

#lst=input("Enter List: ")
#bubsort(list(lst))    

def main():
    lst=[9,7,5,6,8]
    bubsort(lst)
    print('The New List: ')
    print(lst)

if __name__ == '__main__':
    main()
