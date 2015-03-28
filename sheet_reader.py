f1 = open('test1.txt')
f2 = open('test2.txt')

lines = f1.readlines()

for line in lines:
	f2.write(line)

f1.close()
f2.close()