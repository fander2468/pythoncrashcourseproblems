current_users = ['gile', 'aleksander', 'tyrone', 'jennifer', 'sarah']
new_users = ['aleksander', 'SALLY', 'deanna', 'Yolanda', 'johnny']

for new_user in new_users:
    if new_user in current_users:
        print(new_user, 'already used, must enter a different username.')
    elif new_user.upper() in new_users:
        print(new_user.upper(), 'is invalid, must be in all lowercase.')
    elif new_user.title() in new_users:
        print(new_user.title(), 'is invalid, must be in all lowercase.')
    elif new_user not in current_users:
        print(new_user, 'is available.')
