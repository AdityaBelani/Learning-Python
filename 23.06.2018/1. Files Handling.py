#1.Opening a File:
#Syntax: f=open('filename','mode')

#2.Writing to a file:
#syntax: f.write('filename','mode') (Mode shouldn't be 'r')

#3.Reading a file:
#Syntax: f.read()

#4.Closing a file:
#Syntax: f.close()

#Eg.:
f=open('myfile','w')
f.write('Hello World')
f=open('myfile','r') #This line is compulsory to open the file bcz earlier the file was open in 'write' mode. Now it is open in 'read' mode
print(f.read()) #Hello World

#Multiline File:
g=open('MultiLineFile.txt','r')
print(g.readlines()) #['Aditya\n', 'Ashna\n', 'Chetna']
g=open('MultiLineFile.txt','w')
g.writelines('Ashu\nMunmun') 
g=open('MultiLineFile.txt','r')
print(g.readlines()) #['Ashu\n', 'Munmun'] (The file content is updated

#5.Get Pointer Position: Tells the position of file pointer
print(f.tell()) #11
