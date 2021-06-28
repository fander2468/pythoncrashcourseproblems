favorite_guest = ['Marcus Aurelius', 'Albert Einstien', 'Jeshua Ben Joseph']
favorite_guest.insert(0, 'Queen Nefertiti')
favorite_guest.insert(2, 'Bruce Lee')
favorite_guest.append('Steve Jobs')
print('Great ' + favorite_guest[0] + ' I invite you to meet to discus your era.')
print('Hello ' + favorite_guest[2] + ' I invite to meet with you to discus your philsophies and martial arts.')
print('Hi ' + favorite_guest[5] + ' I wish to meet with you to talk about your visions for Apple.')
print('Due to constraints of time I can only invite two guest')
uninvited_guest = favorite_guest.pop()
print('Sorry ' + uninvited_guest + ' I can not invite you to meet for dinner.')
uninvited_guest = favorite_guest.pop()
print('Sorry ' + uninvited_guest + ' I can not invite you to meet for dinner.')
uninvited_guest = favorite_guest.pop()
print('Sorry ' + uninvited_guest + ' I can not invite you to meet for dinner.')
uninvited_guest = favorite_guest.pop()
print('Sorry ' + uninvited_guest + ' I can not invite you to meet for dinner.')
print('I want to thank ' + favorite_guest[0] + ' and ' + favorite_guest[1] + ' for their acceptance and look forward to seeing them during dinner.')
del favorite_guest[1]
del favorite_guest[0]
print(favorite_guest)#this is a test to ensure that the list is empty
