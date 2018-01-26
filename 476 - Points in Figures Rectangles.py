'''
20180126	jlhung	v1.0
'''

a = []
while True:
	n = input()
	if n == "*":
		break
	
	n = list(n.split())
	m = [n[0]]
	m += list(map(float, n[1:]))
	a.append(m)	

c = 1
while True:
	x, y = map(float, input().split())
	if x == 9999.9 and y == 9999.9:
		break
	
	check = 1
	for i in range(len(a)):
		if a[i][1] < x and x < a[i][3] and a[i][2] > y and y > a[i][4]:
			print("Point {} is contained in figure {}".format(c, i+1))
			check = 0
	
	if check:
		print("Point {} is not contained in any figure".format(c))
	
	c += 1
		

