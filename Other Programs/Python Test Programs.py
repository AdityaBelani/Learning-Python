print("Hello!")
user= input("What is your name: ")
age= int(input("What is your age: "))
marks= float(input("Enter your marks: "))
print("My name is",user)
print("My age is",age)
print("My mark is",marks)

#This is a single line comment
'''This is a multi line comment'''

#Integers or Float Data Types:
a=1 #Python automatically declares it as integer
b=int("1") #Integer is declared
c=1.5 #Python automatically declares it as float
d=float("1.5") #Float is declared
print(a,b,c,d)

#String Data Type:
e="This is a string"
f='This is also a string'
print(e,"\n",f)

#List in python- We can input any data type in a list (Use print command for output)
numbers=[1,2,3,4,"x"]
print("Given values are:",numbers)
print(len(numbers))
#5
print(numbers[0]) #index=0
#1
print(numbers[0:2]) #index=0to2
#[1,2]
print(numbers[2:]) #index=2toEnd
#[3,4,x]

#Escape Sequence
g="Aditya\'s"

#Increment & Decrement
h=10 #10
h += 1 #11 (h+1)
h -= 1 #9  (h-1)
i=h**2 #100 (h to the power 2)

#Control Flow
grade=80
if grade>=90:
    if grade==100:
        print("A+")
    else:
        print("A")
elif grade>=80:
    print ("B")
else:
    print("Fail")

#Printing Range of value
for j in range(10): #Prints values 0to9
    print(j)
for k in range(10,20): #Prints values 10to19
    print(k)

l=["a","b","c","d"]
print("The given letters are:\n") #\n=New Line
for i in l:
    print(i)
input()

#While Loop
m=0
while m<100:
    print(m)
    m +=1

n=1
while n<15:
    print(n)
    n +=1

input() #Requires user input to end the command

#Function Declaration
def calc():
    o=int(input("o="))
    p=int(input("p="))
    print("Sum=",o+p)
    print("Diff=",o-p)

calc() #Calls this function 1st time
calc() #Calls this function 2nd time
