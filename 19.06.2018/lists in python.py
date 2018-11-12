#Mutable Objects can be changed, while Immutable can't

#Python List are mutable
#Eg
sub=['Hindi','Eng','Maths']
print(sub) #['Hindi', 'Eng', 'Maths']
sub[2]='Phy'
print(sub) #['Hindi', 'Eng', 'Phy']
print(id(sub)) #58502040

x=5
print(id(x)) #1651263184
x1=x
print(id(x1)) #1651263184
#Both variables share same ID

#Finding values inside 2D List
subcodes=[['Maths',75],['Eng',68],['Hindi',57]]
print(subcodes, #[['Maths', 75], ['Eng', 68], ['Hindi', 57]]
      subcodes[1], #['Eng', 68]
      subcodes[1][0], #Eng
      subcodes[1][1]) #68

details=eval(input('Enter details: '))
print(details)
#eval:Input is always in string format, eval converts to integer form.
