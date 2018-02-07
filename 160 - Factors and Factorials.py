'''
20180207	jlhung	v1.0
'''

a = [0 for i in range(105)]
a[0], a[1] = 1, 1
for i in range(105):
	if a[i] == 0:
		for j in range (i+i, 105, i):
			a[j] = 1
			
while True:
	n = int(input())
	if n == 0:
		break
	
	b = [0 for i in range(105)]
	for k in range(2, n+1):
		m = k
		for i in range(2, k+1):
			if a[i] == 0:
				while m % i == 0:
					m /= i
					b[i] += 1
	
	c = 0
	print("{:3d}! =".format(n), end="")
	for i in b:
		if i > 0:
			if c != 0 and c % 15 == 0:
				print()
				print("      {:3d}".format(i), end="")
			else:
				print("{:3d}".format(i), end="")
			c += 1
	
	print()