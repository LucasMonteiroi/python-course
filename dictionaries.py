# We will use dictonaries and some methods
person = {'name': 'Lucas', 'age': 27, 'country':'Brazil'}
print('Person: ' + str(person))
print('Person Keys: ' + str(person.keys()))
print('Person Values: ' + str(list(person.items())))

print()
print('Formated values')
print()
for k, v in person.items() :
    print(str(k) + ': ' + str(v))

print()
print('Search values')
print()

if 'name' in person :
    print('Field name found in person with value: ' + person['name'])

print('Age found in person with value: ' + str(person.get('age', 0)))

print('Hello my name is ' + str(person['name']) + ', with ' + str(person['age']) + ' old and I am from ' + str(person['country']))

print('Setting default value age to 28')
person.setdefault('age', 28)
print(person)