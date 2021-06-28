active = True
while active:
    message = input('Enter your age and I will tell you how much for a ticket, enter False to quit. ')
    message = int(message)
    if message <= 2:
        print('The ticket is free')
    elif message <= 12:
        print('The ticket will be $10 dollars')
    elif message >= 13:
        print('The ticket will be $15 dollars')
    elif message == 'quit':
        active = False
