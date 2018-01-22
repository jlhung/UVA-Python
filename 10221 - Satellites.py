'''
20180122	jlhung	v1.0
'''

import math

while True:
	try:
		a = list(input().split())
	except EOFError:
		break
		
	s = float(a[0]) + 6440
	if a[2] == 'min':
		a = float(a[1]) / 60
	else:
		a = float(a[1])
	
	if a > 180:
		a = 360 - a
	
	print("{:.6f} {:.6f}".format(a*math.acos(-1)/180*s, 2*s*math.sin(a*math.acos(-1)/180/2)))