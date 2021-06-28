favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

take_poll = ['jen', 'edward', 'jose', 'theresa']

for poll in take_poll:
    if poll in favorite_languages:
        print('Thanks ' + poll.title() + ' for taking the time to take the poll.')
    elif poll not in favorite_languages:
        print('Hello ' + poll.title() + ' please take soem time to take the poll.')
