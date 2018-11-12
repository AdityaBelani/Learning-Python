t1=('Monday','Tuesday')
t2=(10,20,30)

print(t1*2) #('Monday', 'Tuesday', 'Monday', 'Tuesday')

t3=t1+('Wednesday',)
print(len(t3)) #3

print(t2[-2]) #20

#Slicing:
print(t1[1:2]) #('Tuesday',)

#membership Operator:
print('friday' in t1) #False

#Count,Max:
age=(20,18,17,18,15,18,18)
print(age.count(18)) #4
print(age.index(18)) #1
































