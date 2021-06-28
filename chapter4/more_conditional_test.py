user_names = ['tyrone', 'john', 'ebony', 'sarah']
ebony_age = 28
banner_users = 'james'
if user_names[0] != 'gildan':
    print('Sorry your\'re not the right user for this account')

if user_names[1] == 'john':
    print('Hello', user_names[1], 'welcome to your account')

if user_names[3] != 'sarah':
    print('Hello', user_names[3].lower(), 'welcome to your account.')
else:
    print('Hello', user_names[3].title(), 'welcome to your account.')

if len(user_names) == 4 and user_names[2] == 'ebony':
    print(user_names[3].title(), 'is the name of one of the usernames')

if len(user_names) == 4:
    print('All available usernames are used up.')
else:
    print('Username count is:', len(user_names))

if 'tyrone' in user_names:
    print('One of the users names is tyrone' )


if banner_users not in user_names:
    print('None of the users in the list are banned')


