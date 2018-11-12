#Union,intersection,difference,symmetric diff of sets:

fruits={'Apple','Orange','Tomato','Cucumber','Watermelon'}
print(fruits) #{'Cucumber', 'Tomato', 'Watermelon', 'Apple', 'Orange'}
vegetables={'Cucumber','Potato','Tomato','Watermelon','Cauliflower'}
print(vegetables) #{'Cucumber', 'Tomato', 'Potato', 'Watermelon', 'Cauliflower'}

eatables=fruits.union(vegetables)
print(eatables) #{'Cucumber', 'Tomato', 'Potato', 'Watermelon', 'Apple', 'Cauliflower', 'Orange'}
eatables=fruits|vegetables
print(eatables) #{'Cucumber', 'Tomato', 'Potato', 'Watermelon', 'Apple', 'Cauliflower', 'Orange'}

frandveg=fruits.intersection(vegetables)
print(frandveg) #{'Watermelon', 'Tomato', 'Cucumber'}

onlyfruits=fruits-vegetables
print(onlyfruits) #{'Apple', 'Orange'}
onlyfruits=fruits.difference(vegetables)
print(onlyfruits) #{'Apple', 'Orange'}

fruitsXORveg=fruits.symmetric_difference(vegetables)
print(fruitsXORveg) #{'Potato', 'Cauliflower', 'Apple', 'Orange'}
