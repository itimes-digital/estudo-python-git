from user_module import User
from user_profile import *

user1 = User('anderson', 'de sousa', 40, 'são paulo', '11 969-696-696')
user1.describe_user()
user1.greet_user()

user2 = User('bruno', 'mars', 34, 'los angeles, estados unidos', '11 969-969-696-696')
user2.describe_user()
user2.greet_user()

user3 = User('jay', 'z', 50, 'los angeles, estados unidos', '11 111-111-696-696')
user3.describe_user()
user3.show_login_attempts()
user3.greet_user()
print("Realizando vários logins...")
tentativas = 9
login_realizado = 0

while login_realizado < tentativas:
	user3.increment_login_attempts()
	login_realizado += 1
	
login_realizado = 0
user3.show_login_attempts()
user3.reset_login_attempts()
user3.show_login_attempts()
		
ad = Admin()
ad.privileges.show_privileges()
