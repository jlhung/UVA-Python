'''
20180127	jlhung	v1.0
'''

n = int(input())
for i in range(n):
	m = int(input())
	
	x = 0
	y = m
	while y > 0:
		x += (y % 10) ** 2
		y //= 10
	
	a = [0 for j in range(1000)]
	a[1] = 1
	while a[x] == 0:
		a[x] = 1
		
		y = x
		x = 0
		while y > 0:
			x += (y % 10) ** 2
			y //= 10
	
	if x == 1:
		print("Case #{}: {} is a Happy number.".format(i+1, m))
	else:
		print("Case #{}: {} is an Unhappy number.".format(i+1, m))
