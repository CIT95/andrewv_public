import pprint

# create a dict called dog with all the stats of my dog
dog = {'Name':'Kandi','Breed': 'Pitbull','Sex': 'Female','Age': 10,'Color':'Brindle'}
# checking if the 'color' key is a part of my dict could have also used setDefault
if 'Color' in dog:
    print('Color is in the dictionary')
else:
    print('Color is not in the dictionary')
# loop to print all the key value pairs in my dict
for k,v in dog.items():
    print((k,v))
# make a list and populate it with dogs
dogs = []
dogs.append(dog)
dogs.append({'Name':'Tico','Breed': 'Pitbull','Sex': 'Male','Age': 13,'Color':'White/Gray'})
dogs.append({'Name':'Kona','Breed': 'Black Mouth Curr','Sex': 'Female','Age': 2,'Color':'Tan'})
dogs.append({'Name':'Lucy','Breed': 'Australian Cattle Dog','Sex': 'Female','Age': 2,'Color':'Black/White'})
dogs.append({'Name':'Lady','Breed': 'Beagle','Sex': 'Female','Age': 13,'Color':'White/Tan'})
dogs.append({'Name':'Vegas','Breed': 'American Bulldog','Sex': 'Female','Age': 1,'Color':'White/Black'})
dogs.append({'Name':'Biscuit ','Breed': 'Chihuahua/Terrier','Sex': 'Male','Age': 1,'Color':'Tan/White'})
dogs.append({'Name':'Buster','Breed': 'Long Haired Dachshund','Sex': 'Male','Age': 3,'Color':'Black/Tan'})
dogs.append({'Name':'Oliver','Breed': 'Chihuahua/Terrier','Sex': 'Male','Age': 1,'Color':'White'})
# lists to hold male and female dogs
maleDogs = []
femaleDogs = []
# function to format my print out
def printDog(dog):
    for d in dog:
        # prints the basic info of each dog
        print('Name: ' + d['Name'] + '\n  Breed: ' + d['Breed'] + '\n  Sex: ' + d['Sex'] + '\n  Age: ' + str(d['Age']))
# filter the dogs list by sex
for dog in dogs:
    if 'Male' in dog.values():
        maleDogs.append(dog)
    else:
        femaleDogs.append(dog)

# pprint.pprint(dogs)
# make a new list of dogs that is sorted ny age first then by name it is in desending order
sortedDogs = sorted(dogs, key = lambda x: (x['Age'], x['Name']),reverse=True)
# pprint.pprint(dogs)
""" print('Male dogs:')
printDog(maleDogs)
print('Female dogs:')
printDog(femaleDogs) """
printDog(sortedDogs)
totalNumberOfDogs = 0
totalAge = 0
averageAge = 0
maxAge = 0
minAge = 900
# finding the average, min, and max ages
for dog in sortedDogs:
    totalNumberOfDogs += 1
    totalAge += dog['Age']
    if maxAge < dog['Age']:
        maxAge = dog['Age']
    if minAge > dog['Age']:
        minAge = dog['Age']

print('Total number of dogs I know: ' + str(totalNumberOfDogs))
print('Average age of the dogs I know: ' + str((int)(totalAge/totalNumberOfDogs)))
print('The Max age of the dogs I know: ' + str(maxAge))
print('The Min age of the dogs I know: ' + str(minAge))