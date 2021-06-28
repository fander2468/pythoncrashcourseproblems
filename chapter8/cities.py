def describe_city(country, city):
    print(city + ' is in the ' + country)

describe_city('United States', 'Seattle')

def describe_city_default(city_name, country = 'Ghana'):
    print(city_name + ' is in the ' + country)

describe_city_default('Accra')