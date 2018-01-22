'''
20180122	jlhung	v1.0
'''

while True:
	try:
		n = int(input())
	except EOFError:
		break
		
	a = []
	for i in range(n):
		a.append(int(input()))
		
	a.sort()
	x = a[(n - 1) // 2]
	y = a[n // 2]
	
	c = 0
	for i in range(n):
		if a[i] == x or a[i] == y:
			c +=1
	
	d = y - x + 1
	print(x, c, d)