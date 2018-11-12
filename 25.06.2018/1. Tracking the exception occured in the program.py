import sys
def main():
    try:
        f=open('Temp-File','r')
    except IOError as err:
        print('Problem with Output...\n',err)
        print(sys.exc_info())
    print('Program continues after the Try Block...')
if __name__ == '__main__':
    main()
