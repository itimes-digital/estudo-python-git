from car import Car

my_new_car = Car('audi', 'a4', 2016)
print("\n" + my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.fill_gas_thank()

your_new_car = Car('ford', 'focus', 2016)
print("\n" + your_new_car.get_descriptive_name())
your_new_car.odometer_reading = 30
your_new_car.read_odometer()

other_new_car = Car('volks', 'fusca', 1975)
print("\n" + other_new_car.get_descriptive_name())
other_new_car.update_odometer(100)
other_new_car.read_odometer()
#else
other_new_car.update_odometer(20)

other_new_car.increment_odometer(35)
other_new_car.read_odometer()
