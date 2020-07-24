from pypet import Pypet

print('welcome to pypet')

mypet = Pypet('fluffy',3,2.0,'(=^0.0^=)__')

mypet.speak()
mypet.feed()
mypet.speak()
mypet.play()
mypet.speak()


# For long running lines, we break them in Python using the \ character
# also you had forgotten the commas between {} items
pet_collection = \
[{"name": "fishy","age":1, "weight": 0.3, "photo":">++('>'"}, \
{"name": "mickey", "age":91, "weight": 0.5, "photo": "<.3 )~~~~"}, \
{'name':'fishbones', 'age':12, 'weight': 0.5, 'photo':'< )))><'}, \
{'name': 'vampy', 'age': 125, 'weight': 80.4, 'photo':'(^0M0^)'}]


# We can't name this array the same (pet) as the ariable you use below.
# So I renamed it to pets
pets = []

for pet in pet_collection:
    newpet = Pypet(pet['name'],pet['age'],pet['weight'],pet['photo'])
    newpet.speak()
    pets.append(newpet)
                                                                                                                                                                                                                                                                                                                                                                                                                                                           