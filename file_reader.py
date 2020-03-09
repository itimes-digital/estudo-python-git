path_file = 'C:\\Users\\admin\\Documents\\estudos\\text-file\\titanic_test.csv'
#path_file = 'C:\\Users\\admin\\Documents\\estudos\\text-file\\pi_digits.txt'
with open(path_file) as file_object:
	lines = file_object.readlines()

count = 1
for line in lines:
	if line[8:9] == 'C':
		print("Linha lida " + str(count) + ": " + line)
		count += 1
#print(contents.rstrip())#elimina linha em branco no final do arquivo

print('\n')

count = 1
for line in lines:
	if line[8:9] == 'Z':
		line = line.replace('Zakarian', 'Didi')
		print("Linha lida " + str(count) + ": " + line)
		count += 1
#print(contents.rstrip())#elimina linha em branco no final do arquivo

print('\n')

unique_lines = ''
for line in lines:
	if line[8:9] == 'A':
		unique_lines += line.strip() + " - "
		#unique_lines += line.lstrip() + " - "
		#unique_lines += line.rstrip() + " - "
		
print("Linhas lidas em uma única linha : " + unique_lines)
print(len(unique_lines))

for line in lines:
	unique_lines += line.rstrip()
		
birthday = input('Enter your birthday, in the form mmddyy: ')
if birthday in unique_lines:
	print("Your birthday appers in the first million of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")


