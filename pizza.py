def make_pizza(size, *toppings):
	"""Apresenta a pizza que estamos prestes a preparar"""
	print('\nmaking a ' + str(size) 
		+ '-inch pizza with the following toppings:')
	for topping in toppings:
		print('- ' + topping)
