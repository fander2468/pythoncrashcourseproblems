users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    'ndtyson': {
        'first': 'neil',
        'last': 'degrasse tyson',
        'location': 'new york',
        },
 }

for username, user_info in users.items():
  print("\nUsername has the info of: " + username)
  full_name = user_info['first'] + " " + user_info['last']
  location = user_info['location']
  print("\tFull name: " + full_name.title())
  print("\tLocation: " + location.title())