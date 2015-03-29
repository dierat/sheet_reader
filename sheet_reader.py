f1 = open('101_radicals.csv', 'r')
f2 = open('chars.txt', 'w')


lines = f1.readlines()

f2.write('chars = [\n')

for i in range(len(lines)):
	temp_string = '['
	temp_array = lines[i].split(',', 5)
	for j in range(len(temp_array)):
		if j == 4:
			temp_array[4] = temp_array[2].replace(' ', '_') + '.' + temp_array[4]
		if j == 5:
			descrip = temp_array[j]
			edited_descrip = ''
			for k in range(len(descrip)):
			 	if k != 0 and k != (len(descrip) - 1) and k != (len(descrip) - 2):
			 		if descrip[k] != '"' and descrip[k] != "'":
			 			edited_descrip += descrip[k]
			 		if descrip[k] == '\'':
			 			edited_descrip += '\\' + "'"
			 		if descrip[k] == '"':
			 			if descrip[k + 1] != '"':
			 				edited_descrip += descrip[k]
			temp_array[j] = edited_descrip
		temp_string = temp_string + "'" + temp_array[j] + "'"
		if j != len(temp_array) - 1:
			temp_string = temp_string + ','
	temp_string = temp_string + ']'
	if i != len(lines) - 1:
		temp_string = temp_string + ',\n'
	f2.write(temp_string)

f2.write('\n];')
		

f1.close()
f2.close()