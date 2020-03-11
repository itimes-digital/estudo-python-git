"""Executando exception"""
print("Give me two numbers, and I'll divide them")
print("Enter 'q' to quit")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	try:#try-except-else
		answer = int(first_number)/int(second_number)
	except ZeroDivisionError:
		print('Prezado usuário, não é possível dividir por zero(0)!')
	else:
		print(answer)

filename = 'C:\\Users\\admin\\Documents\\estudosXXX\\text-file\\guest.txt'

try:
	with open(filename) as obj_open:
		contents = obj_open.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + "does not exist."
	print(msg)
