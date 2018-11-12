import re
st1='Welcome to the Python Programming'
match=re.search('Python',st1)
match.group() #'Python'
match=re.search('(P|p)ython',st1)
match=re.search('Py*',st1)
match=re.search('Py?',st1)

str1='Python is a powerful lang'
if re.search('^Python',str1):
print('starts with python') #starts with python

string='abc12ccaab'
match=re.search('a(b|c)*\d[1,2]c*',string)
match.group() #'abc12cc'
