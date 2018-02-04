'''
20180204	jlhung	v1.0
'''

a = ["BCG", "BGC", "CBG", "CGB", "GBC", "GCB"]

while True:
	try:
		b0, g0, c0, b1, g1, c1, b2, g2, c2 = map(int, input().split())
	except EOFError:
		break
	
	b = [0 for i in range(6)]
	b[0] = b1 + b2 + c0 + c2 + g0 + g1
	b[1] = b1 + b2 + g0 + g2 + c0 + c1
	b[2] = c1 + c2 + b0 + b2 + g0 + g1
	b[3] = c1 + c2 + g0 + g2 + b0 + b1
	b[4] = g1 + g2 + b0 + b2 + c0 + c1
	b[5] = g1 + g2 + c0 + c2 + b0 + b1

	min = 0
	for i in range(1, 6):
		if b[min] > b[i]:
			min = i
	print("{} {}".format(a[min], b[min]))