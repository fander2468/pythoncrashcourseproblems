names = ['tyrone', 'billy', 'ebony', 'sarah', 'jennifer', 'admin']
names = []
if names:
    for name in names:
        if name != 'admin':
            print('Hello', name, 'thank you for logging in again')
        elif name == 'admin':
            print('Hello', name, 'would you like to see a status report.')
        else:
            print('This username is not listed')
else:
    print('We need to find some users.')