#Set Functions: add,update,remove,pop,clear

vehicles=set(['Bike','Car','Bicycle','Scooter'])
print(vehicles) #{'Car', 'Scooter', 'Bike', 'Bicycle'}

vehicles.add('Bus')
print(vehicles) #{'Bicycle', 'Bike', 'Car', 'Scooter', 'Bus'}

vehicles.remove('Car')
print(vehicles) #{'Bicycle', 'Bike', 'Scooter', 'Bus'}

vehicles.pop()
print(vehicles) #{'Bike', 'Scooter', 'Bus'}

vehicles.clear()
print(vehicles) #set()
