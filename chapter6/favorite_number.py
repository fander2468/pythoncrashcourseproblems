favorite_numbers = {'sally': [7, 14], 'jonas': [12, 15], 'jensen': [17, 25], 'jose': [3, 12], 'mercedes': [21, 19]}
for name, favorite_number in favorite_numbers.items():
    print('Favorite numbers of ' + name)
    for numbers in favorite_number:
        print(numbers)