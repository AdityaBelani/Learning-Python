def binarysearch(lst,searchval):
    low,high=0,len(lst)-1
    while low<=high:
        mid=int((low+high)/2)
        if lst[mid]==searchval:
            return mid
        elif searchval<lst[mid]:
             high=mid-1
        else:
            low=mid+1
    return None

def issorted(lst):
    for i in range(1,len(lst)):
        if lst[i]<lst[i-1]:
            return False
    return True

def main():
    lst=list(input('Enter a Sorted List(ascending orderr): '))
    if not(issorted(lst)):
        print('Given List is not sorted.')
    else:
        searchval=input('Enter the value to be searched... ')
        print(searchval,'Found at Index',binarysearch(lst,searchval))

main()
