persons_age = 41

if persons_age < 2:
    print('Person is a baby.')
elif persons_age >= 2 and persons_age < 4:
    print('Person is a toddler.')
elif persons_age >= 4 and persons_age < 13:
    print('Person is kid')
elif persons_age >= 13 and persons_age < 20:
    print('Person is a teenager')
elif persons_age >= 20 and persons_age < 66:
    print('Person is a adult.')
else:
    print("Person is a elder")