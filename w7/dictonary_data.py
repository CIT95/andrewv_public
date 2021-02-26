myCat = {'size':'fat','color':'gray', 'disposition':'loud'}

print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')

spam = {12345: 'Luggage combination', 42 : 'The Answer'}

print([1,2,3] == [3,2,1])

eggs = {'name': 'Zophie', 'species':'cat', 'age':8}
ham = {'species': 'cat', 'name' : 'Zophie', 'age':8}

print(eggs == ham)

print('name' in eggs)

print(list(eggs.keys()))
print(list(eggs.values()))

for k,v in eggs.items():
    print((k,v))

print(eggs.get('age',0))
print(eggs.get('color',''))
picnicItems = {'apples' : 5, 'cups' : 2}
print('I am bringing ' + str(picnicItems.get('napkins',0)) + ' napkins to the picnic')

eggs.setdefault('color', 'black')
print(eggs)
eggs.setdefault('color', 'orange')
print(eggs)

