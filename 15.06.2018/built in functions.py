#Built in functions on strings:

#Count:
'Encyclopedia'.count('c') #Counts the occurence of char'c', output=2

#find & replace:
colors='green,red,green,blue,green,red'
colors.find('red') #6
colors.rfind('red') #27 (right find)

msg='Knp is a big city.'
msg.replace('Knp','Lko')

#Lower,Upper,istitle:
#title case: eg. This Is A Good Book
#sentence case: eg. This is a good book
st='Kanpur'
st.istitle() #True

#Strip,lstrip,rstrip:
'   Hello Hi   '.lstrip()

#Splt & Partition
colors='Red,Green,Blue,Orange,Yellow,Cyan'
colors.split(',') #Space is the default delimiter
'Hello.How are You?'.partition('.') #('Hello', '.', 'How are You?')
' '.join(['I','am','ok']) #'I am ok'

#isspace,isalpha,isdigit,isalnum:
#It checks only 1st character
#alnum=alpha numeric
nm='ABCD'
nm.isalpha() #True

#startswith,endswith:
nm='Sanjay'
nm.startswith('Dr.') #False

#Encoding & Decoding:
str='Secret Message'.encode('utf32') #utf8, utf16 can also be used
str.decode('utf32') #'Secret Message' (Same decoding scheme has to be used)
