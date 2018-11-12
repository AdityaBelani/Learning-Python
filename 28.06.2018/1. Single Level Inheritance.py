#Simple Inheritance

class Employee(object):
    def __init__ (self,EmpNo,EmpName,EmpDesign,EmpContact):
        self.EmpNo=EmpNo
        self.EmpName=EmpName
        self.EmpDesign=EmpDesign
        self.EmpContact=EmpContact
    def show(self):
        print('Employee No.: ',self.EmpNo)
        print('Employee Name: ',self.EmpName)
        print('Employee Designation: ',self.EmpDesign)
        print('Employee Contact No.: ',self.EmpContact)

#In Class Salary all the members of Class Employee are inherited.

class Salary(Employee):
    def __init__ (self,EmpNo,EmpName,EmpDesign,EmpContact,Basic,Hra,Da):
        '''In Python name of the base class can be used to access the Base class methods, Here base class constructor accept EmpNo, EmpName, EmpDesign, EmpContact, we pass these values.'''
        Employee. __init__ (self,EmpNo,EmpName,EmpDesign,EmpContact)
        self.Basic=Basic
        self.Hra=Hra
        self.Da=Da
    def showSalary(self):
        print('Basic Salary: ',self.Basic)
        print('HRA: ',self.Hra)
        print('DA: ',self.Da)
        print('Net Salary: ',self.Basic+self.Hra+self.Da)

EmpSal=Salary(101,'A. B.','Manager',1234567890,10000,1500,2000)
EmpSal.show() #Calling Base class method using sub class object
EmpSal.showSalary()
