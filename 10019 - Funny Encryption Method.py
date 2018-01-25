'''
20180125	jlhung	v1.0
'''

n = int(input())
for _ in range(n):
	m = int(input())
	
	a, b = 0, 0
	z = m
	while z > 0:
		if z % 2 == 1:
			a += 1
		z //= 2
	
	x = 0
	while m > 0:
		x = m % 10 + x * 16
		m //= 10
	while x > 0:
		if x % 2 == 1:
			b += 1
		x //= 2
		
	print(a, b)