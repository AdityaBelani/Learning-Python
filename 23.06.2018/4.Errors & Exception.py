#1.Name Error: It is found whenever a name that appearss in the statement is not found globally.
#Eg.: 'input' is wriiten as 'Input'

#2.Type Error: When Python func is applied to an inappropriate data type.
#Eg.: 'Sum of 2 & 3 is'+5

#3.Value Error:
#Eg.: int('Hello')

#4.Zero Division Error:
#Eg.: a=5,b=0,c=a/b

#5.OS Error: When file is opened in read mode, but file doesn't exist

#6.Index Error:

def main():
    try:
        f=open('temp','r')
    except IOError:
        print('Problem with I/O')
    print('Program continues after the block')
if __name__ == '__main__':
    main()
