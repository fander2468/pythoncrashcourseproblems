sandwich_orders = ['tunafish', 'meatball', 'pastrami', 'ham', 'pastrami', 'turkey', 'samon', 'pastrami']
finished_sandwiches = []
print('The deli has run out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for sandwich_order in sandwich_orders:
    print('I made your ' + sandwich_order + ' sandwich.')
    finished_sandwiches.append(sandwich_order)

print('\n')

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich + ' sandwich has been completed.')