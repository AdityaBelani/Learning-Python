try:
    f=open('Temp-File','r')
except IOError:
    print('Prob with Input Output...\n')
else:
    print('No Prob\n')
