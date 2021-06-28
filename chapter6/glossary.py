programming_glossary = {'variable': 'used to store data for later use',
                        'conditional': 'used to decide if code should be run',
                        'list': 'used to store more than one data kind',
                        'dictionary': 'used to store data in key-value pairs',
                        'loops': 'used to repeat an action until condition is false'}

#print('variable ' + programming_glossary['variable'] + '\n' +
 #     'conditional ' + programming_glossary['conditional'] + '\n' +
 #     'dictionary ' + programming_glossary['dictionary'] + '\n' +
 #     'list ' + programming_glossary['list'] + '\n' +
 #     'loops ' + programming_glossary['loops'] + '\n' )

for key, value in programming_glossary.items():
      print(key, value)