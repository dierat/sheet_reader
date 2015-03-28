f1 = open('101_radicals.csv', 'r')
f2 = open('test2.txt', 'w')

lines = f1.readlines()

for i in range(len(lines)):
	if i % 2 == 0:
		f2.write(lines[i])

f1.close()
f2.close()