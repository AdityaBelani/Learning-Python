#Pickle: used when working on structures
import pickle
def main():
    f=open('file1','wb')
    pickle.dump(['hello','world'],f)
    pickle.dump({1:'one',2:'two'},f)
    f.close()
    f=open('file1','rb')
    value1=pickle.load(f)
    value2=pickle.load(f)
    print(value1,value2)
    f.close()
if __name__ == '__main__':
    main()

#Output: ['hello', 'world'] {1: 'one', 2: 'two'}
