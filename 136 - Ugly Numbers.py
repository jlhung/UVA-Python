'''
20180122	jlhung	v1.0
'''

a = [1]
x, y, z = 0, 0, 0
for i in range(1, 1500):
	while True:
		if a[x] * 2 > a[i-1]:
			break
		x += 1
	while True:
		if a[y] * 3 > a[i-1]:
			break
		y += 1
	while True:
		if a[z] * 5 > a[i-1]:
			break
		z += 1
		
	n = min(a[x]*2, a[y]*3)
	n = min(n, a[z]*5)
	a.append(n)
	
print("The 1500'th ugly number is {}.".format(a[1499]))