def printtab(num,nmult=10):
    for n in range(1,nmult+1):
        product=num*n
        print(num,'*','%2d'%n,'=','%5d'%product)
def main():
    num=int(input('Enter a no.: '))
    printtab(num)
if __name__ == '__main__':
    main()
