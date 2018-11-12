#For loop used with assert
#str does Numeric to Character conversion
#range(lower bound, upper bound-1)

def main():
    n=int(input('Enter the no. of subjects: '))
    tot=0
    print ('Enter marks: ')
    for i in range(1,n+1):
        marks = float(input('Subject' + str(i) + ':'))
        assert marks>=0 and marks<=100
        tot+=marks
    per=tot/n
    print('Percentage= ',per)
if __name__ == '__main__':
    main()
