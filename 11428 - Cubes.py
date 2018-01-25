'''
20180125	jlhung	v1.0
'''

while True:
	n = int(input())
	if n == 0:
		break
	
	x, y = 1, 1
	while x ** 3 < n:
		x += 1
		
	while True:
		if x**3 - (x-1)**3 > n:
			print("No solution")
			break
		
		if x**3 - y**3 == n:
			print(x, y)
			break
		else:
			if x - 1 == y:
				x += 1
				y = 1
			else:
				y += 1
			
			
		