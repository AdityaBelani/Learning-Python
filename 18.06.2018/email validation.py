#This will search for only 1st occurence
import re
match=re.search(r'[a-z0-9]+(\.[a-z0-9]+)*@[a-z]+(\.[a-z]+)+', 'ram@gmail.com, pranav.gupta@cs.iitd.ac.in, nik@yahoo.com, raman@gmail.com')
print(match.group()) #'ram@gmail.com'

#This will search every string
for i in re.finditer(r'[a-z0-9]+(\.[a-z0-9]+)*@[a-z]+(\.[a-z]+)+', 'ram@gmail.com, pranav.gupta@cs.iitd.ac.in, nik@yahoo.com, raman@gmail.com'):
    print(i.group())
'''ram@gmail.com
pranav.gupta@cs.iitd.ac.in
nik@yahoo.com
raman@gmail.com'''
