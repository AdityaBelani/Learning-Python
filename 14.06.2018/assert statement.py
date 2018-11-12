#Assert Statement: Used to validate inputs

def per(mark,maxmark):
    per1=(mark/maxmark)*100
    return per1
def main():
    maxmark=float(input('Enter Max Marks:'))
    assert maxmark>=0 and maxmark<=500
    marks=float(input('Enter the Marks: '))
    assert marks<=maxmark and marks>0
    per1=per(marks,maxmark)
    print('Percentage= ',per1)
if __name__ == '__main__':
    main()
