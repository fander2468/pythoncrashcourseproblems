num = input('Please enter a number and I will tell you if it is a multiple of ten. ')
num = int(num)
if num % 10 == 0:
    print(str(num) + ' is a multiple of ten.')
else:
    print(str(num) + ' is not a multiple of ten.')