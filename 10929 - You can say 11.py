'''
20171216	jlhung	v1.0
'''

while True:
	n = input()
	
	if n == '0':
		break

	x = y = 0
	for i in range(0, len(n)):
		if i % 2:
			x += int(n[i])
		else:
			y += int(n[i])

	if abs(x-y) % 11:
		print("%s is not a multiple of 11." %n)
	else:
		print("%s is a multiple of 11." %n)