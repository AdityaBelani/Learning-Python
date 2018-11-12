#Passing of list as argument

def listupdate(a,i,value):
    a[i]=value

def main():
    lst=[10,20,30,40,50]
    listupdate(lst,1,27)
    print(lst)

if __name__ == '__main__':
    main()
