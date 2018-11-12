#Shalow Copy: When the value is changed in list 1, value of list 2 is also changed.
#Method 1:
list1=[10,20,[30,40]]
list2=list1
print(list2) #[10, 20, [30, 40]]
list1.remove(20)
print(list1) #[10, [30, 40]]
print(list2) #[10, [30, 40]]

#Deep Copy: When the value is changed in list 1, value of list 2 is NOT changed.
#Method 2:
import copy
list1=[10,20,30]
list2=copy.copy(list1)
print(list2) #[10, 20, 30]
list1.remove(30)
print(list1) #[10, 20]
print(list2) #[10, 20, 30]

#Method 3:
import copy
list1=[10,20,30]
list2=copy.deepcopy(list1)
print(list2) #[10, 20, 30]
list1.remove(30)
print(list1) #[10, 20]
print(list2) #[10, 20, 30]
