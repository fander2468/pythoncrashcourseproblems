person1 = {'first_name': 'adam', 'last_name': 'nelson', 'age': 37, 'city': 'paige', 'state': 'arizona'}
person2 = {'first_name': 'johnny', 'last_name': 'fenelus', 'age': 42, 'city': 'barstow', 'state': 'california'}
person3 = {'first_name': 'alicia', 'last_name': 'gleeson', 'age': 24, 'city': 'san fransisco', 'state': 'california'}

people = [person1, person2, person3]

for person in people:
      print('A person I know is named ' + person['first_name'].title() + ' ' +
         person['last_name']. title() + ', he is ' + str(person['age']) + 
         ' and lives in ' + person['city'].title() + ' '+ person['state'].title() +'.')
