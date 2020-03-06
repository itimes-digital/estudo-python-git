from random import randint

class Die():
	
	def __init__(self, sides=6):
		self.sides = sides
		
	def roll_die(self):
		print(randint(1, self.sides))
		
my_die_6 = Die()
count = 0
print('\n')
while count < 10:
	my_die_6.roll_die()
	count += 1

my_die_10 = Die(10)
count = 0
print('\n')
while count < 10:
	my_die_10.roll_die()
	count += 1

my_die_20 = Die(20)
count = 0
print('\n')
while count < 10:
	my_die_20.roll_die()
	count += 1
