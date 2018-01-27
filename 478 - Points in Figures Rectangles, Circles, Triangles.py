'''
20180127	jlhung	v1.0
'''

import math

def dist(*b):
	return math.sqrt((b[0] - b[2])**2 + (b[1] - b[3])**2)
	
def area(*b):
	x = dist(b[0], b[1], b[4], b[5])
	y = dist(b[0], b[1], b[2], b[3])
	z = dist(b[2], b[3], b[4], b[5])
	s = (x + y + z) / 2
	return math.sqrt(s * (s-x) * (s-y) * (s-z))
	

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
		if a[i][0] == "r":
			if a[i][1] < x and x < a[i][3] and a[i][2] > y and y > a[i][4]:
				print("Point {} is contained in figure {}".format(c, i+1))
				check = 0
		elif a[i][0] == "c":
			if a[i][3] > dist(a[i][1], a[i][2], x, y):
				print("Point {} is contained in figure {}".format(c, i+1))
				check = 0
		else:
			all_area = area(a[i][1], a[i][2], a[i][3], a[i][4], a[i][5], a[i][6])
			area_a = area(x, y, a[i][1], a[i][2], a[i][5], a[i][6])
			area_b = area(x, y, a[i][1], a[i][2], a[i][3], a[i][4])
			area_c = area(x, y, a[i][3], a[i][4], a[i][5], a[i][6])
			
			if area_a == 0 or area_b == 0 or area_c == 0:
				continue
			if abs(all_area - area_a - area_b - area_c) < 0.001:
				print("Point {} is contained in figure {}".format(c, i+1))
				check = 0
			
	
	if check:
		print("Point {} is not contained in any figure".format(c))

	
	c += 1
