f1=open('myfile','r')
f2=open('myfileCopy','w')
data=f1.read()
f2.write(data)
f1.close()
f2.close()
f2=open('myfileCopy','r')
print(f2.read()) #Hello World
