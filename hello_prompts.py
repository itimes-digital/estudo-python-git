message = input("Tell me something, and I will repeat it back to you: ")
print(message)

message = input("Please enter your first name: ")
print("Hello, " + message + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your second name? "

name = input(prompt)
print(message + " " + name)

age = input("How old are you? ")
print(age)

if int(age) > 18:
	print("its oldest")
else:
	print("its newest")
	
height = input("How tall are you, in centimeter? ")
height = int(height)

if height >= 36:
	print("\nYou´re tall enough to ride!")
else:
	print("\nYou're tall enough to ride!")
	
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print("\n" + str(pets))

while 'cat' in pets:
	pets.remove('cat')

print(pets)
