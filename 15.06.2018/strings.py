#printing a charaacter from the string

msg='Hello Knp'
msg
msg[0]
msg[3]
msg[7]
len(msg) #finds length of
index=len(msg)-1 #len(msg)=9, reduces 1=8
msg[index]
msg[-1] #It will start going backwards, i.e -1=last element, -2=2nd last element
msg[1]='k' #Gives Error, bcz strings are mutable, i.e can't be changed

'Hi'+'Knp' #HiKnp
'Hi'*3 #HiHiHi

max('mum','agr','Alh') #mun
min('mum','agr','Alh') #Alh
