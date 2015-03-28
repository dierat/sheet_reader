f1 = open('101_radicals.csv', 'r')
f2 = open('test2.txt', 'w')


lines = f1.readlines()

f2.write('chars = [')

for line in lines:
	temp_array = line.split(',')
	temp_string = '['
	for i in range(len(temp_array)):
		temp_string = temp_string + "'" + temp_array[i] + "'"
		if i != len(temp_array) - 1:
			temp_string = temp_string + ','
	temp_string = temp_string + ']'
	f2.write(temp_string)

f2.write(']')
		

f1.close()
f2.close()