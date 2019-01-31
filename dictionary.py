from collections import defaultdict

## initializing a default dictionary will means that even keys that do not yet exist will have this default value
cities = defaultdict(lambda: 'OTHER')


cities['madrid'] = 'this is madrid'
cities['valencia'] = 'I am valencia'

print(cities['madrid'])
print(cities['valencia'])

# note that the key torino is not present in the dictionary, and it will have the default value OTHER
print(cities['torino'])


