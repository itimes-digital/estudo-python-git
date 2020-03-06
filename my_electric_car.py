from car import Car, ElectricCar
#from car import *

my_beetle = Car('Volks', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

print('\n')

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_thank()
my_tesla.battery.get_range()

print('\n')

other_tesla = ElectricCar('tesla', 'model s', 2020)
print(other_tesla.get_descriptive_name())
other_tesla.battery.describe_battery()
other_tesla.battery.get_range()
other_tesla.battery.upgrade_battery()
other_tesla.battery.get_range()




