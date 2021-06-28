def make_shirt(message, size = 'large'):
    print('I love ' + message + ' shirt size ' + size)

make_shirt('Python')

def make_shirt_sizes(size, message = 'Python is awesome'):
    print('Shirt size is ' + size + ' shirt message is ' + message)

make_shirt_sizes('large')
make_shirt_sizes('small')
make_shirt_sizes('medium')