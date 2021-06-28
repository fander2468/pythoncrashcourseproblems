magicians = ['Harry Houdini', 'David Blaine', 'David Coperfield']

def show_magicians(names):
    for name in names:
        message = 'Welcome ' + name
        print(message)

show_magicians(magicians)

def make_great(great_magician):
    print('\n')
    for great in great_magician:
        print('The Great ' + great)

make_great(magicians[:])# Will make a copy however not pass the actual list