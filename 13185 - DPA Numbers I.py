'''
20180103	jlhung	v1.0
'''

n = int(input())
for i in range(n):
	m = int(input())
	
	c = 0
	for j in range(1, (m//2)+1):
		if m % j == 0:
			c += j

	if c > m:
		print("abundant")
	elif c == m:
		print("perfect")
	else:
		print("deficient")