def nMatchedchar(str1,str2):
    temp1=str1.lower()
    temp2=str2.lower()
    count=0
    for ch1 in temp1:
        for ch2 in temp2:
            if ch1==ch2:
                count+=1
    print(count)
def main():
    n1='RAM'
    n2='rom'
    nMatchedchar(n1,n2)

if __name__ == '__main__':
    main()

#Output: 2
#It will compare both the strings for having same characters. It is not necessary that both should be in same order. n2 can also be 'mor'
