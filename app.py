from pypet import Pypet

print('welcome to pypet')

mypet =Pypet ('fluffy',3,2.0,'(=^0.0^=)__')

mypet.speak()
mypet.feed()
mypet.speak()
mypet.play()
mypet.speak()


pet_collection = \
[{"name": "fishy","age":1, "weight": 0.3, "photo":">++('>'"}
{"name": "mickey", "age":91, "weight": 0.5, "photo": "<.3 )~~~~"}
{'name':'fishbones', 'age':12, 'weight': 0.5, 'photo':'< )))><'}
{'name': 'vampy', 'age': 125, 'weight': 80.4, 'photo':'(^0M0^)'}]


pet =[]

for pet in pet_collection:
    newpet = Pypet(pet['name'],pet['age'],pet['weight'],pet['photo'])
    newpet.speak()
    pet.append(newpet)
                                                                                                                                                                                                                                                                                                                                                                                                                                                           