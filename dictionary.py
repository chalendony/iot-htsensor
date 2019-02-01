# whenever you need a dictionary, and each element’s value should start with a default value, use a defaultdict.
from collections import defaultdict

## initializing a default dictionary will means that every key that does not yet exist will have the default value ‘OTHER’
cities = defaultdict(lambda: 'OTHER')

## assign values to dictionary keys
cities['madrid'] = 'this is madrid'
cities['valencia'] = 'I am valencia'

## lets see what we get?
print('madrid: {}'.format(cities['madrid']))
print('valencia: {}'.format(cities['valencia']))

# now access a key, that was not *explicitly* apriori
# note that the key ‘torino’ is not *yet* present in the dictionary, and it will have the default value OTHER
print('torino: {}'.format(cities['torino']))

# now lets see whats in our dictionary
print('what''s in my dictionary:  {}'.format(cities))