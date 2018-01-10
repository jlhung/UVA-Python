'''
20171216	jlhung	v1.0
'''

n = int(input())
case = 0

for i in range(0, n):
	x = int(input())
	y = int(input())
	if x > y:
		x, y = y, x
	
	sum = 0
	case += 1
	for j in range(x, y+1):
		if j % 2:
			sum += j
		
	print("Case {0}: {1}".format(case, sum))