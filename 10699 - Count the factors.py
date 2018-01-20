'''
20180120	jlhung	v1.0
'''

import math

while True:
	n = int(input())
	if n == 0:
		break
	
	c = 0
	d = n
	i = 2
	while i < math.sqrt(n):
		if n % i == 0:
			c += 1
		while n % i == 0:
			n /= i
		i += 1
	if n != 1:
		c += 1
	print("{} : {}".format(d, c))
	