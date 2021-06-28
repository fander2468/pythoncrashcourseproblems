def make_car(model, make, **car_info):
    car = {}
    car['model'] = model
    car['make'] = make
    for info in car_info.items():
        car['info'] = info
    return car




car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)