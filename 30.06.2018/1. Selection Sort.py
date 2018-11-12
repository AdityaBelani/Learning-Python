def selsort(lst):
    for i in range(0,len(lst)-1):
        for j in range(i,len(lst)):
            if lst[j]<lst[i]:
                t=lst[j]
                lst[j]=lst[i]
                lst[i]=t
    print('The new List')
    print(lst)

lst=input("Enter List: ")
selsort(list(lst))    
