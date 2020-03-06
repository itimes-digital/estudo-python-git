from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
favorite_languages['other'] = 'java'

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + 
		language.title() + ".")
		
print('Regular dictionary: ')
d = {}#Possivelmente em ordem
d['a'] = 'A'
d['b'] = 'B'
d['z'] = 'Z'
d['c'] = 'C'

for k, v in d.items():
	print(k, v)
	
print('\nOrderedDict: ')
d = OrderedDict()#Sempre em ordem
d['a'] = 'A'
d['b'] = 'B'
d['z'] = 'Z'
d['c'] = 'C'

for k, v in d.items():
	print(k, v)

