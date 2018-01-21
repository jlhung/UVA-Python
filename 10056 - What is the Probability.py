'''
20180121	jlhung	v1.0
'''

import math

n = int(input())
for i in range(n):
	n, p, k = map(float, input().split())
	
	if p == 0:
		print("0.0000")
	elif k == 1:
		print("{:.4f}".format(p / (1 - math.pow(1-p, n))))
	else:
		print("{:.4f}".format(p * math.pow(1-p, k-1) / (1 - math.pow(1-p, n))))