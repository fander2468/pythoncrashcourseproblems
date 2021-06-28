vaction_spots = {}
active = True

while active:
    user = input('Please enter your name: ')
    location = input('Please enter a spot you woulr like to visit: ')
    vaction_spots[user] = location

    repeat = input("Are there any other users:(yes/no) ")
    if repeat == 'no':
        active = False
    
print('Here are the results!')

for user, location in vaction_spots.items():
    print(user.title() + ' wants to visit ' + location.title())