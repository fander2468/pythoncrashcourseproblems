cities = {'seattle': {'state': 'washington', 'country': 'united states', 'population_millions': 3.4} ,
          'san francisco': {'state': 'california', 'country': 'united states', 'population_millions': 3.3 }, 
          'Raliegh': {'state': 'north carolina', 'country': 'united states', 'population_millions': 1.4}}

for city, info in cities.items():
    print(city + ':')
    all_info = info['state'] + ' ' + info['country'] + ' ' + str(info['population_millions'])
    print(all_info + '\n')
