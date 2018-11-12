#Multiplication Operand (*):
#int1=eval(input('Enter details: ')) #['ajay',20,'knp']
#print(int1*2) #['ajay', 20, 'knp', 'ajay', 20, 'knp']

#Concatenation:
list1=['red','green','blue']
list2=list1+['grey']
print(list2) #['red', 'green', 'blue', 'grey']

#Len:
print(len(list1)) #3 (bcz indexing starts from 0)

#Indexing:
print(list1[-1]) #blue

#Slicing:
print(list1[0:5:2]) #['red', 'blue']
print(list1[5:0:-2]) #['blue']
#SYNTAX: listname(st:end:inc)

#Membership Operand:
print(40 in list1) #False

st=['Ram','Ajay','Amit','Manu','Pankaj']
for nm in st:
    print (nm)
'''Output:
Ram
Ajay
Amit
Manu
Pankaj'''

mk={50,65,72,47,96,30}
cnt=0
for marks in mk:
    if marks>=60:
        cnt+=1
print(cnt) #3

nm=['Amit','Ram','manoj']
print(nm) #['Amit', 'Ram', 'manoj']

nm.insert(1,'Alok')
print(nm) #['Amit', 'Alok', 'Ram', 'manoj']

nm.sort()
print(nm) #['Alok', 'Amit', 'Ram', 'manoj']

nm.reverse()
print(nm) #['manoj', 'Ram', 'Amit', 'Alok']

print(nm.count('manoj')) #1 (No. of times that item exists)

nm.append('gita')
print(nm) #['manoj', 'Ram', 'Amit', 'Alok', 'gita']

nm.remove('Ram')
print(nm) #['manoj', 'Amit', 'Alok', 'gita']
