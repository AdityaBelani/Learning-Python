import re
#Finds the value with same pattern
print(re.findall(r'[A-Za-z]+ing','Walking down the road,he was thinking about the coming years')) #['Walking', 'thinking', 'coming'])

#Split
print(re.split(r',','Mirza,Rohit,Vivek')) #',|\n' can also be used. Output:['Mirza', 'Rohit', 'Vivek']

addr='B-6,Lodhi Road,Delhi'
print(len(addr),
      addr[17:1],
      addr[-len(addr):len(addr)],
      addr[:-12]+addr[12:],
      addr.find('Delhi'),
      addr.swapcase(),
      addr.split(','),
      addr.isalpha())
