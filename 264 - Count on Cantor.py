'''
20180201	jlhung	v1.0
'''

while True:
	try:
		n = int(input())
	except EOFError:
		break
		
	x, y = 1, 1
	while y < n:
		x += 1
		y += x
	
	p = 1 + y - n
	q = x - p + 1
	print("TERM {} IS ".format(n), end="")
	if x % 2 == 1:
		print("{}/{}".format(p, q))
	else:
		print("{}/{}".format(q, p))